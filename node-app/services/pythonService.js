const axios = require('axios');

const PYTHON_BASE_URL = 'http://localhost:5001';

async function getSessionHistory(userId) {
    const response = await axios.get(`${PYTHON_BASE_URL}/get_session_history/${userId}`);
    return response.data;
}

async function updateSession(data) {
    const response = await axios.post(`${PYTHON_BASE_URL}/update_session`, data);
    return response.data;
}

module.exports = {
    getSessionHistory,
    updateSession,
};