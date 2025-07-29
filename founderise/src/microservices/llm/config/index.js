// Configuration setup for LLM Microservice

const dotenv = require('dotenv');
dotenv.config();

module.exports = {
  port: process.env.LLM_PORT || 3001,
  apiKey: process.env.LLM_API_KEY || '',
  apiEndpoint: process.env.LLM_API_ENDPOINT || '',
  defaultLLM: process.env.DEFAULT_LLM || 'AzureOpenAI',
};

