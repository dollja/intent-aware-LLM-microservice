from flask import Flask, request, jsonify
import redis
import json
from textblob import TextBlob  # For sentiment analysis
import openai

# Flask app initialization
app = Flask(__name__)

# Redis client initialization
redis_client = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)

# OpenAI API Key
openai.api_key = "YOUR_API_KEY"  # Replace with your OpenAI API key

def save_session(user_id, data):
    """Save session data to Redis."""
    redis_client.set(f"user_session:{user_id}", json.dumps(data))

def get_session(user_id):
    """Retrieve session data from Redis."""
    session_data = redis_client.get(f"user_session:{user_id}")
    return json.loads(session_data) if session_data else []

def analyze_sentiment(text):
    """Analyze sentiment of user input."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment

def generate_trust_aware_response(user_input, session_history):
    """Generate a multi-level intent-aware LLM response using ToM and Appraisal Theory."""
    try:
        # Constructing the prompt with Theory of Mind and Appraisal Theory
        system_prompt = """
        You are a multi-level intent-aware assistant designed to foster trust and rapport in human-AI teams.
        Use Theory of Mind to anticipate how your actions and decisions will affect trust and rapport levels.
        Apply Appraisal Theory to assess the significance of your actions within the context of the team's goals,
        and adapt your behavior to maintain a stable and trust-rich collaboration environment.
        """
        
        # Adding session history for context
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "system", "content": f"Session History: {session_history}"},
            {"role": "user", "content": user_input}
        ]

        # OpenAI ChatCompletion API Call
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use GPT-4 for advanced capabilities
            messages=messages
        )
        
        # Extracting the response content
        response_content = response["choices"][0]["message"]["content"]
        
        # Dummy appraisal analysis for illustration
        appraisal = f"The response aligns with the team's goals of fostering trust and rapport."
        
        return response_content, appraisal
    except Exception as e:
        return f"Error generating response: {str(e)}", "No appraisal available"

@app.route('/update_session', methods=['POST'])
def update_session():
    """Update the session and generate a trust-aware response."""
    data = request.json
    user_id = data['user_id']
    user_input = data['user_input']

    # Retrieve session history
    session_history = get_session(user_id)

    # Analyze sentiment
    sentiment = analyze_sentiment(user_input)

    # Generate trust-aware response
    response, appraisal = generate_trust_aware_response(user_input, session_history)

    # Update session
    session_entry = {
        "input": user_input,
        "output": response,
        "sentiment": sentiment,
        "appraisal": appraisal
    }
    session_history.append(session_entry)
    save_session(user_id, session_history)

    return jsonify({"response": response, "appraisal": appraisal, "sentiment": sentiment})

@app.route('/get_session_history/<user_id>', methods=['GET'])
def get_session_history(user_id):
    """Retrieve session history for a user."""
    return jsonify(get_session(user_id))

if __name__ == "__main__":
    app.run(port=5001)
