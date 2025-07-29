// Import required dependencies
const express = require('express');

// Create a new router instance
const router = express.Router();
const axios = require("axios");

// In-memory store for LLM configurations (temporary for development purposes)
const llmConfigurations = [];

// POST route to add a new LLM configuration
router.post('/addLLM', (req, res) => {
    const { name, apiKey, endpoint } = req.body;

    // Validate request body
    if (!name || !apiKey || !endpoint) {
        return res.status(400).json({ error: 'Missing required fields: name, apiKey, endpoint' });
    }

    // Save to the in-memory store
    llmConfigurations.push({ name, apiKey, endpoint });

    // Respond with success
    return res.status(201).json({ message: 'LLM configuration added successfully', data: { name, apiKey, endpoint } });
});

// GET route to list all LLM configurations
router.get('/listLLM', (req, res) => {
    // Respond with the current list of LLM configurations
    res.status(200).json({
        message: 'List of configured LLMs retrieved successfully',
        data: llmConfigurations
    });
});

// Export the router
module.exports = router;

// GET route to check the health of external LLM APIs
router.get('/llmHealth', async (req, res) => {
    const results = [];
    for (const llm of llmConfigurations) {
        try {
            const response = await axios.get(llm.endpoint, {
                headers: { 'Authorization': `Bearer ${llm.apiKey}` }
            });
            results.push({ name: llm.name, status: 'healthy', details: response.data });
        } catch (error) {
            results.push({ name: llm.name, status: 'unhealthy', error: error.message });
        }
    }
    res.status(200).json({
        message: 'LLM health check completed',
        results
    });
});

