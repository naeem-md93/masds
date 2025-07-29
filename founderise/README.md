```markdown
# Multi-Agent Software Development System

A state-of-the-art collaborative platform that orchestrates multiple specialized software agents to simplify and automate various stages of software development. This system accelerates software creation, testing, deployment, database synchronization, user authentication, and even updates its own documentation. It is designed to boost developer productivity with modularity, scalability, and seamless integration between its components.

---

## Features

- **Multi-Agent Architecture**:  
  Utilizes specialized agents to handle distinct development tasks, enabling scalability and modularity.

- **Frontend ConversationPage Revamp**:  
  - Enhanced `src/frontend/pages/ConversationPage.js` to use actual APIs for conversation handling.  
  - Integrated endpoints for synchronizing conversation logs and interacting with the LLM microservice.

- **Google OAuth Integration**:  
  - Secure, user-friendly login/logout functionality with Google OAuth, implemented in the frontend `AuthPage.js`.

- **LLM Microservice**:  
  - Configurable integration with AI models like Azure OpenAI.  
  - Includes health-check endpoints and dynamic endpoint management.

- **Persona Management API**:  
  - CRUD functionality for creating, managing, and deleting personas.  
  - Dynamically adjust agent behaviors based on persona configurations.

- **Database Synchronization**:  
  - Enables seamless synchronization between PostgreSQL and MongoDB databases.  
  - Includes an SQL-based `conversation_logs` table to capture API-driven chat logs.

- **Robust Health Monitoring**:  
  - Monitors availability of key services via `/health` endpoints.

- **JWT Authentication Middleware**:  
  - Token validation for secure API communication and resource protection.

- **Customizable Configuration**:  
  - Environment variable-driven setup for authentication secrets, LLM endpoints, database connections, and more.

- **Solid Developer Tooling**:  
  - Includes workflows for testing (`npm test`), linting (`npm run lint`), and building (`npm run build`) to ensure maintainable code.

---

## Recent Changes

### 1. Improved ConversationPage UI (Task: #15)  
Enhanced the `ConversationPage.js` to fetch and send user messages using actual backend APIs. Integrated the following endpoints:  
- **Conversation API**: Redirected to `/api/database/sync` for synchronizing conversation data with the database.  
- **LLM Message API**: Redirected to `/api/llm/addLLM` for LLM-based user interaction.

Example Component Update:
```jsx
fetch('/api/database/sync')
  .then(response => response.json())
  .then(data => console.log(data));

fetch('/api/llm/addLLM', {
  method: 'POST',
  body: JSON.stringify({ message: userMessage }),
  headers: { 'Content-Type': 'application/json' }
})
  .then(response => response.json())
  .then(result => console.log(result));
```

---

### 2. Google OAuth Integration  
Secure Google login/logout capability introduced in `AuthPage.js`. 

Example buttons:
```jsx
<div>
  <button onClick={handleGoogleLogin}>Login with Google</button>
  <button onClick={handleLogout}>Logout</button>
</div>
```

---

### 3. Persona Management API  
CRUD API for managing configurable personas:
```bash
# Create a persona
curl -X POST http://localhost:<AGENTS_PORT>/personas \
-H "Content-Type: application/json" \
-d '{"name": "Developer", "role": "Backend Engineer", "description": "Handles API design"}'

# Retrieve all personas
curl http://localhost:<AGENTS_PORT>/personas
```

---

## Setup & Installation

### Prerequisites
Ensure the following dependencies are installed:
- **Node.js v18+**  
- **PostgreSQL** (running instance)  
- **MongoDB** (running instance)  
- A Google OAuth Client (`Client ID` and `Client Secret`).  

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-organization/multi-agent-development-system.git
   cd multi-agent-development-system
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure the `.env` file:
   ```bash
   cp .env.example .env
   ```
   Fill in values like `JWT_SECRET`, `DATABASE_URL`, `GOOGLE_CLIENT_ID`, etc.

4. Set up databases:
   Ensure PostgreSQL and MongoDB services are running, then initialize the database structures:
   ```bash
   npx sequelize-cli db:migrate
   ```

---

## Running the Application

Start the main application:
```bash
npm run start
```

This will initialize the frontend, backend microservices, and database sync functionalities.

### Example API Interactions
1. **Login via Google OAuth**  
   Visit the UI at `http://localhost:<FRONTEND_PORT>` and click "Login with Google."

2. **Synchronize Conversations**:  
   ```bash
   curl -X POST http://localhost:<AGENTS_PORT>/syncDatabase
   ```

3. **Check Microservice Health**:  
   ```bash
   curl http://localhost:<AGENTS_PORT>/health
   ```

---

## Configuration

### Required Environment Variables

Below are the key environment variables required to configure the system:

| Variable                | Description                                     |
|-------------------------|-------------------------------------------------|
| `JWT_SECRET`            | Secret key for secure JWT authentication.       |
| `DATABASE_URL`          | PostgreSQL connection string.                  |
| `LLM_API_KEY`           | API key for Azure OpenAI Service integration.  |
| `LLM_API_ENDPOINT`      | URL endpoint for Azure OpenAI service.         |
| `LLM_PORT`              | Running port for the LLM microservice.         |
| `AGENTS_PORT`           | Running port for the agents microservice.      |
| `GOOGLE_CLIENT_ID`      | OAuth client ID for Google authentication.     |
| `GOOGLE_CLIENT_SECRET`  | OAuth client secret for Google authentication. |
| `POSTGRES_HOST`         | PostgreSQL instance hostname.                  |
| `POSTGRES_PORT`         | PostgreSQL port number.                        |
| `POSTGRES_USER`         | User for accessing PostgreSQL.                 |
| `POSTGRES_PASSWORD`     | PostgreSQL account password.                   |
| `POSTGRES_DB`           | Target database in PostgreSQL.                 |
| `MONGO_URL`             | Connection string for MongoDB.                 |
| `MONGO_DB_NAME`         | Target database in MongoDB.                    |

---

## Developer Workflows

### Testing
Run the test suite:
```bash
npm test
```

### Code Linting
Ensure clean code with lint checks:
```bash
npm run lint
```

### Build for Production
Generate a production-ready build:
```bash
npm run build
```

---

## Contributing

Contributions are welcomed! To contribute:
1. Fork the repository and create a feature branch (e.g., `feature/new-feature-x`).  
2. Follow coding and documentation standards, ensuring all tests pass.  
3. Open a pull request and provide a detailed description of your changes.  

Refer to the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```