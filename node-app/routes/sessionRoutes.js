const express = require('express');
const router = express.Router();
const { getSessionHistory, updateSession } = require('../services/pythonService');

router.get('/session/:userId', async (req, res) => {
    try {
        const userId = req.params.userId;
        const sessionHistory = await getSessionHistory(userId);
        res.json(sessionHistory);
    } catch (error) {
        res.status(500).send('Error fetching session history');
    }
});

router.post('/session/update', async (req, res) => {
    try {
        const { userId, userInput, modelOutput, inferredIntent } = req.body;
        const result = await updateSession({
            user_id: userId,
            user_input: userInput,
            model_output: modelOutput,
            inferred_intent: inferredIntent,
        });
        res.json(result);
    } catch (error) {
        res.status(500).send('Error updating session');
    }
});

module.exports = router;