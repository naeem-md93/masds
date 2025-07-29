// Import required dependencies
const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');
require('dotenv').config();
const syncDatabaseRouter = require('./routes/syncDatabase');
const healthRouter = require('./routes/health');

// Initialize the Express app
const app = express();

// Middleware
app.use(cors());
app.use(healthRouter);
app.use(bodyParser.json());
app.use(syncDatabaseRouter);

// Health check endpoint
app.get('/health', (req, res) => {
    res.status(200).json({ status: 'Database Service is healthy' });
});

// Port configuration
const PORT = process.env.DATABASE_PORT || 3003;

// Start the server
app.listen(PORT, () => {
    console.log(`Database Microservice is running on port ${PORT}`);
});
