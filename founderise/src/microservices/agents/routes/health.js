// Import required dependencies
const express = require('express');

// Create a new router instance
const router = express.Router();

// Define the health check route
router.get('/health', (req, res) => {
    res.status(200).json({
        status: 'Agents Microservice is healthy',
        timestamp: new Date().toISOString()
    });
});

// Export the router
module.exports = router;
