from flask import Flask, request, jsonify
import redis
import json
from textblob import TextBlob  # For sentiment analysis

app = Flask(__name__)
redis_client = redis.StrictRedis(host="localhost", port=6379, decode_responses=True)

def save_session(user_id, data):
    redis_client.set(f"user_session:{user_id}", json.dumps(data))

def get_session(user_id):
    session_data = redis_client.get(f"user_session:{user_id}")
    return json.loads(session_data) if session_data else []

def analyze_sentiment(text):
    """Analyze the sentiment of the user's input."""
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment

@app.route('/update_session', methods=['POST'])
def update_session():
    data = request.json
    user_id = data['user_id']
    user_input = data['user_input']
    model_output = data['model_output']
    inferred_intent = data['inferred_intent']

    # Analyze sentiment
    sentiment = analyze_sentiment(user_input)

    session = get_session(user_id)
    session.append({
        "input": user_input,
        "output": model_output,
        "intent": inferred_intent,
        "sentiment": sentiment
    })
    save_session(user_id, session)

    return jsonify({"status": "success", "sentiment": sentiment})

@app.route('/get_session_history/<user_id>', methods=['GET'])
def get_session_history(user_id):
    return jsonify(get_session(user_id))

@app.route('/explain_response', methods=['POST'])
def explain_response():
    """Provide an explanation for the model's response."""
    data = request.json
    user_input = data['user_input']
    response = data['model_output']
    intent = data['inferred_intent']
    explanation = f"The response aligns with your input '{user_input}' because it matches the inferred intent '{intent}'."
    return jsonify({"explanation": explanation})

if __name__ == "__main__":
    app.run(port=5001)