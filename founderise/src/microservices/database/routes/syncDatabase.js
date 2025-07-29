// Import required dependencies
const express = require('express');
const { Sequelize } = require('sequelize');
const { MongoClient } = require('mongodb');

// Create a new router instance
const router = express.Router();

// Define PostgreSQL and MongoDB connection details
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

// Connect to PostgreSQL
const connectPostgres = async () => {
    const sequelize = new Sequelize(postgresConfig.database, postgresConfig.username, postgresConfig.password, {
        host: postgresConfig.host,
        port: postgresConfig.port,
        dialect: 'postgres',
    });
    await sequelize.authenticate();
    return sequelize;
};

// Connect to MongoDB
const connectMongoDB = async () => {
    const client = new MongoClient(mongoConfig.url);
    await client.connect();
    const db = client.db(mongoConfig.dbName);
    return { client, db };
};

// Sync logic for databases
const syncDatabases = async () => {
    const postgres = await connectPostgres();
    const mongo = await connectMongoDB();
    const mongoClient = mongo.client;
    const mongoDb = mongo.db;
    
    try {
        console.log('Fetching data from PostgreSQL...');
        const [users] = await postgres.query('SELECT * FROM users');
        console.log('Fetched users:', users.length);

        console.log('Syncing data with MongoDB...');
        await mongoDb.collection('users').deleteMany({});
        await mongoDb.collection('users').insertMany(users.map((user) => ({
            username: user.username,
            email: user.email,
            createdAt: user.createdAt,
            updatedAt: user.updatedAt
        })));
        
        console.log('Sync complete!');
        return {
            message: 'Databases synced successfully',
            postgres: users.length,
            mongo: await mongoDb.collection('users').countDocuments()
        };
    } finally {
        await postgres.close();
        await mongoClient.close();
    }
};

// Define the sync database route
router.post('/syncDatabase', async (req, res) => {
    try {
        const result = await syncDatabases();
        res.status(200).json({
            status: 'success',
            message: result.message,
            postgresCount: result.postgres,
            mongoCount: result.mongo
        });
    } catch (error) {
        console.error('Error syncing databases:', error);
        res.status(500).json({
            status: 'error',
            message: 'Failed to sync databases',
            error: error.message
        });
    }
});

// Export the router
module.exports = router;
