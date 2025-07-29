// Import required dependencies
const express = require('express');

// Create a new router instance
const router = express.Router();

// Define the health check route
router.get('/health', (req, res) => {
    res.status(200).json({ status: 'LLM Microservice is healthy' });
});

// Export the router
module.exports = router;
