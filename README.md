# Multi-level intent-aware LLM
A multi-level intention-aware LLM that uses Theory of Mind to anticipate how its decisions and actions will affect human rapport  levels. The model integrates appraisal theory to assess the significance of these actions within the context of the team's goals and then adapts its behavior to enable the integration of individual mental states into collective, coherent views and decisions.

--
### **Key Features*

#### **1. Multi-Level Intent-Aware Responses**
- **Theory of Mind (ToM)**:
  - LLM generates responses anticipating how they will impact **trust and rapport**.
  - Incorporates **session history** to maintain consistency and adapt to the user's evolving needs.

- **Appraisal Theory**:
  - The model evaluates:
    1. The **relevance** of the user's input.
    2. How its response supports the **team's goals**.
    3. The **emotional impact** of the response.

#### **2. OpenAI API Integration**
- The `generate_trust_aware_response` function uses OpenAI's `ChatCompletion` endpoint with `gpt-4`.
- The system prompt explicitly instructs the LLM to prioritize trust-building and goal alignment.

#### **3. Sentiment and Appraisal in Session History**
- Session entries now include:
  - **Sentiment** of the user input.
  - **Appraisal** of the response's alignment with trust and rapport.

---

### **Sample Interaction**

#### **Scenario**
A user interacts with the assistant to discuss collaboration challenges in a team.

1. **User Input**:
   ```
   How can I better support my teammates in our project?
   ```

2. **Generated Response**:
   ```
   Supporting your teammates starts with understanding their goals and challenges. 
   Consider setting up regular check-ins to foster open communication and trust.
   Would you like suggestions for structuring these check-ins?
   ```

3. **Sentiment**:
   - Neutral

4. **Appraisal**:
   - "The response aligns with the team's goals of fostering trust and rapport."

5. **Session History**:
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
