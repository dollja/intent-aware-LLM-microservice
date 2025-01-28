
# Multi-Level Intent-Aware Microservice App

## Overview
 A multi-level intention-aware LLM that uses theory of mind to anticipate how its decisions and actions will affect human rapport levels. The model integrates appraisal theory to assess the significance of these actions within the context of the team's goals, then adapts its behavior to enable the integration of individual mental states into collective, coherent views and decisions.

--


### Key Features:
- Session-Aware Responses: Maintains user interaction history to generate consistent and context-aware responses.
- Sentiment Analysis: Analyzes the emotional tone of user inputs for better understanding.
- Trust and Rapport Management: Uses ToM to anticipate how responses affect trust and rapport levels.
- Appraisal Theory Integration: Evaluates how responses align with team goals and emotional impact.
- Explainable AI: Provides explanations for how responses align with inferred user intentions.

---

## Planning

### Requirements:
- Python 3.8 or later
- Node.js 14.x or later
- Redis (for session management)
- OpenAI API Key (for GPT-4 integration)

### Components:
1. Python Backend:
   - Handles OpenAI API interactions.
   - Performs sentiment analysis and response appraisal.
   - Stores session history in Redis.
2. Node.js/Express Backend:
   - Serves as the API gateway and hosts the frontend.
   - Communicates with the Python backend.
3. Frontend:
   - A minimal web interface to interact with the AI assistant.
   - Displays session history, sentiments, and appraisals.

---

## Setup

### Local Installation and Run

#### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/trust-aware-app.git
cd trust-aware-app
```

#### 2. Set Up the Python Backend
1. Navigate to the `python-backend` folder:
   ```bash
   cd project-root/python-backend
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\\Scripts\\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Redis server (if not already running):
   ```bash
   redis-server
   ```
5. Start the Python backend:
   ```bash
   python python_backend.py
   ```

#### 3. Set Up the Node.js Backend
1. Navigate to the `node-app` folder:
   ```bash
   cd ../node-app
   ```
2. Install Node.js dependencies:
   ```bash
   npm install
   ```
3. Start the Node.js server:
   ```bash
   node app.js
   ```

#### 4. Access the App
- Open your browser and navigate to: `http://localhost:3000`

---

### Deploying to the Cloud (Vercel)

To deploy the Node.js backend and frontend on Vercel and run the Python backend separately:

#### 1. Deploy Node.js App on Vercel
1. Install the Vercel CLI:
   ```bash
   npm install -g vercel
   ```
2. Log in to Vercel:
   ```bash
   vercel login
   ```
3. Navigate to the `node-app` folder:
   ```bash
   cd project-root/node-app
   ```
4. Deploy to Vercel:
   ```bash
   vercel
   ```
   Follow the prompts to configure the deployment.

#### 2. Host Python Backend on a Cloud Server
- Use a cloud provider (e.g., AWS EC2, Heroku, Google Cloud) to host the Python backend:
  1. Install Python and Redis on the server.
  2. Upload the `python-backend` folder to the server.
  3. Start the Python backend:
     ```bash
     python python_backend.py
     ```
- Ensure the Python backend is accessible via a public URL.

#### 3. Update Node.js App with Python Backend URL
- Edit the `services/pythonService.js` file in the `node-app` folder:
  ```javascript
  const PYTHON_BASE_URL = 'https://your-python-backend-url';
  ```

---

## Notes
- Ensure Redis is running before starting the Python backend.
- Replace `"YOUR_API_KEY"` in `python-backend/python_backend.py` with your actual OpenAI API key.
- For secure deployment, use environment variables to store sensitive keys and configurations.
- To enable HTTPS for the Python backend, use tools like NGINX or a reverse proxy.

---
## Sample Interaction

### Scenario
A user interacts with the assistant to discuss collaboration challenges in a team.

1. User Input:
   ```
   How can I better support my teammates in our project?
   ```

2. Generated Response:
   ```
   Supporting your teammates starts with understanding their goals and challenges. 
   Consider setting up regular check-ins to foster open communication and trust.
   Would you like suggestions for structuring these check-ins?
   ```

3. Sentiment:
   - Neutral

4. Appraisal:
   - "The response aligns with the team's goals of fostering trust and rapport."

5. Session History:
   ```
   [
       {
           "input": "How can I better support my teammates in our project?",
           "output": "Supporting your teammates starts with understanding their goals...",
           "sentiment": "Neutral",
           "appraisal": "The response aligns with the team's goals of fostering trust and rapport."
       }
   ]
   ```

---
