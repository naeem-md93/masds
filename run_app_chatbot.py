from masds import develop_a_project


if __name__ == "__main__":
    project_description = """
    I want you to build an chatbot app using Node.js and AzureOpenAI.
    All configurations (e.g. API keys) should be stored and retrieved from a .env file.
    This app should have 3 different microservices. each of them should run on a local server and they should communicate using API calls.
    
    1. The LLM microservice is responsible for managing multiple LLMs (like OpenAI, AzureOpenAI, etc), binding a new LLM, unbinding an existing LLM, checking their health and are they alive. and it should server these LLMs for the Agents Microservice.
    2. The agents microservice is responsible for managing, adding, modifying, and removing persona's. for example, responding to the user request as a doctor, developer, etc.
    3. the third microservice is a database microservice. It is responsible for managing, adding, removing multiple databases (PostgreSQL, MongoDB, MySQL, etc), checking their health and are they alive, and syncing between them. These databases stores the users and their conversations.
    
    This app should have a web page like chatgpt.com where a user can create a new conversation or resume and old one. 

    """

    develop_a_project("founderise", project_description)
