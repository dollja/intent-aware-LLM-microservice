const express = require('express');
const sessionRoutes = require('./routes/sessionRoutes');

const app = express();
app.use(express.json());
app.use('/', express.static('public'));
app.use('/api', sessionRoutes);

app.listen(3000, () => {
    console.log('Node.js server is running on http://localhost:3000');
});