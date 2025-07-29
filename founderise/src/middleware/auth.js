// Import dependencies
const jwt = require('jsonwebtoken');
require('dotenv').config();

// Middleware function to validate JWT tokens
const authenticateJWT = (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({ error: 'Access token is missing' });
  }

  // Verify the provided token
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({ error: 'Invalid or expired token' });
    }
    req.user = user; // Attach decoded user information to the request
    next();
  });
};

// Export the middleware
module.exports = authenticateJWT;
