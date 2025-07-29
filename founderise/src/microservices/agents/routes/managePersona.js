// Import required dependencies
const express = require('express');

// Create a new router instance
const router = express.Router();

// In-memory storage for personas (this should use a proper DB in production)
const personas = [];

// POST endpoint to create a new persona
router.post('/personas', (req, res) => {
    const { name, role, description } = req.body;

    if (!name || !role || !description) {
        return res.status(400).json({ error: 'Missing required fields: name, role, description' });
    }

    const newPersona = {
        id: personas.length + 1,
        name,
        role,
        description
    };
    personas.push(newPersona);
    res.status(201).json({ message: 'Persona created successfully', data: newPersona });
});

// GET endpoint to retrieve all personas
router.get('/personas', (req, res) => {
    res.status(200).json({ data: personas });
});

// DELETE endpoint to remove a persona by ID
router.delete('/personas/:id', (req, res) => {
    const { id } = req.params;
    const index = personas.findIndex(p => p.id === parseInt(id, 10));

    if (index === -1) {
        return res.status(404).json({ error: 'Persona not found' });
    }

    personas.splice(index, 1);
    res.status(200).json({ message: 'Persona deleted successfully' });
});

// PUT endpoint to update a persona by ID
router.put('/personas/:id', (req, res) => {
    const { id } = req.params;
    const { name, role, description } = req.body;

    if (!name || !role || !description) {
        return res.status(400).json({ error: 'Missing required fields: name, role, description' });
    }

    const persona = personas.find(p => p.id === parseInt(id, 10));

    if (!persona) {
        return res.status(404).json({ error: 'Persona not found' });
    }

    persona.name = name;
    persona.role = role;
    persona.description = description;

    res.status(200).json({ message: 'Persona updated successfully', data: persona });
});

// Export the router
module.exports = router;
