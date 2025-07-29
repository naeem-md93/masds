// Import required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
const config = require('./config');
const log = require('./utils/logger');
require('dotenv').config();
const addLLMRouter = require('./routes/addLLM');

// Initialize the Express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(addLLMRouter);

// Health check endpoint
app.get('/health', (req, res) => {
  log('Health endpoint accessed');
  res.status(200).json({ status: 'LLM Service is healthy' });
});

// Port configuration
const PORT = config.port;

// Start the server
app.listen(PORT, () => {
  log(`LLM Microservice is running on port ${PORT}`);
});
