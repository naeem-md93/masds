// Import required dependencies
const express = require('express');
const { Sequelize } = require('sequelize');
const { MongoClient } = require('mongodb');

// Create a new router instance
const router = express.Router();

// Load database configurations
const postgresConfig = {
  host: process.env.POSTGRES_HOST || 'localhost',
  port: process.env.POSTGRES_PORT || 5432,
  database: process.env.POSTGRES_DB || 'postgres',
  username: process.env.POSTGRES_USER || 'user',
  password: process.env.POSTGRES_PASSWORD || 'password'
};

const mongoConfig = {
  url: process.env.MONGO_URL || 'mongodb://127.0.0.1:27017',
  dbName: process.env.MONGO_DB_NAME || 'chatbot'
};

// Health check logic
const checkPostgresHealth = async () => {
  try {
    const sequelize = new Sequelize(postgresConfig.database, postgresConfig.username, postgresConfig.password, {
      host: postgresConfig.host,
      port: postgresConfig.port,
      dialect: 'postgres',
      logging: false,
    });
    await sequelize.authenticate();
    await sequelize.close();
    return { status: 'healthy', message: 'PostgreSQL connection is active' };
  } catch (error) {
    return { status: 'unhealthy', message: error.message };
  }
};

const checkMongoHealth = async () => {
  try {
    const client = new MongoClient(mongoConfig.url);
    await client.connect();
    await client.db(mongoConfig.dbName).command({ ping: 1 });
    await client.close();
    return { status: 'healthy', message: 'MongoDB connection is active' };
  } catch (error) {
    return { status: 'unhealthy', message: error.message };
  }
};

// Define the health check route
router.get('/health', async (req, res) => {
  const postgresHealth = await checkPostgresHealth();
  const mongoHealth = await checkMongoHealth();
  res.status(200).json({
    postgres: postgresHealth,
    mongo: mongoHealth
  });
});

// Export the router
module.exports = router;
