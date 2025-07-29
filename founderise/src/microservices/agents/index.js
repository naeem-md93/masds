// Import required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
require('dotenv').config();
const healthRouter = require('./routes/health');
const managePersonaRouter = require('./routes/managePersona');

// Initialize the Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(healthRouter);
app.use(managePersonaRouter);

// Health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'Agents Service is healthy' });
});

// Port configuration
const PORT = process.env.AGENTS_PORT || 3002;

// Start the server
app.listen(PORT, () => {
    console.log(`Agents Microservice is running on port ${PORT}`);
});
