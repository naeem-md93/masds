const request = require('supertest');
const express = require('express');
const bodyParser = require('body-parser');

// Mock LLM microservice routes
const addLLMRouter = require('../routes/addLLM');
const healthRouter = require('../routes/health');

// Create a test app
const app = express();
app.use(bodyParser.json());
app.use(addLLMRouter);
app.use(healthRouter);

describe('LLM API Routes', () => {
  test('Health endpoint should return 200 with correct status message', async () => {
    const response = await request(app).get('/health');
    expect(response.status).toBe(200);
    expect(response.body).toHaveProperty('status', 'LLM Microservice is healthy');
  });

  test('POST /addLLM should add a new LLM configuration', async () => {
    const llmConfig = {
      name: 'test-llm',
      apiKey: 'test-api-key',
      endpoint: 'https://sample-endpoint.com'
    };
    const response = await request(app).post('/addLLM').send(llmConfig);
    expect(response.status).toBe(201);
    expect(response.body.message).toBe('LLM configuration added successfully');
    expect(response.body.data).toMatchObject(llmConfig);
  });

  test('POST /addLLM should return 400 for missing fields', async () => {
    const response = await request(app).post('/addLLM').send({ name: 'test-llm' });
    expect(response.status).toBe(400);
    expect(response.body.error).toBe('Missing required fields: name, apiKey, endpoint');
  });
});
