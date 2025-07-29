from masds import develop_a_project


if __name__ == "__main__":
    project_description = """
    I want you to create a multi-agent software development system using Python, LangChain, and AzureOpenAI.
    All of your configrations (like API keys) should be in a '.env' file.
    This system should work like this:
    1. At the start, the user will provide a project description and path to the project directory.
    2. The system should initialize a local git repository, at set the `main` as the main branch (if not exists already).
    3. After that, the system should index all the files in the project directory to understand what have done before. and understand the previous implementations. It should index it in a way that is easy to retrieve and modify those files. It can use an agent to summarize each file. You can decide which approach is the best.
    4. One agent should read that project description and previous implementations carefully and writes a PRD (Project Requirements Document) if the description is sufficient. Otherwise It should ask follow-up questions until it has all the information necessary.
    5. After that, another agent should read the PRD and previous implementations and split the project into many tasks. the tasks should be small enough so that an AI-agent can implement it. each task should have a title, a detailed description (indicating what should be done and which files should be changed), and a branch name for this task.
    6. Then In a loop, an orchestrator agent should create and checkout to a task's branch. then it should assign that task to a implementer agent.
    7. The implementation agent should read the task description and the provided files, and implement the task. The implementation agent can create/modify/delete files and directories. It's implementation should be executable. I mean the agent's response should be in a way that can create files and feed contents to those files.
    8. After that the orchestrator agent should review if the implementer agent's response is correct and execuing it won't result in any errors. if an error raises, it should restore all the changes, checkout to the main branch, delete the task's branch and create that branch again and assign that branch to the implementation agent.
    9. If the implementation is correct, the orchestrator agent should commit the changes and checkout to the main branch and update the README.md file describing the newest updates, how the project works and how one should run it.
    10. the orchestrator agent should do these for all tasks until they are all done.
    
(1/11 - What platforms should this system support? For example, is it intended to run locally, on the cloud, or both?
It it intended to run locally.
(2/11 - How should files in the project directory be indexed? Should we use vector-based storage, semantic search, or another method?
I don't know. Do whatever you think is the best.
(3/11 - What is the expected format of the PRD and the subsequent task outputs? Plain text, Markdown, or another structured format?
The PRD is better to be in JSON format
(4/11 - What are the scalability requirements? For instance, should the system handle large-scale codebases efficiently?
not right now. for now the database can be simple.
(5/11 - How should API keys and sensitive data in the `.env` file be secured and managed?
I didn't understand what you ment.
(6/11 - Should agents learn or adapt over time (e.g., reinforcement learning), or are they expected to act purely deterministically and preprogrammed with LangChain/AzureOpenAI capabilities?
For now, make them deterministic. Use AzureOpenAI with carefully designed prompts.
(7/11 - What specific performance benchmarks or constraints must the system meet (e.g., task turnaround time, concurrency)?
for now, the benchmark is not important. But currectly implementing the project is very important.
(8/11 - Should the orchestrator agent support parallel task execution, or is strict sequential task handling required?
for now, it should execute tasks sequentially.
(9/11 - What types of error management and retry mechanisms should be implemented beyond branch restoration?
I don't know any other method. Use whatever method that have more impact on the accuracy of the result.
(10/11 - How should integrations (e.g., AzureOpenAI) be configured to ensure failover or redundancy?
write a .env file that the user should fill the configs.
(11/11 - What are the expectations for documentation? Should the system produce detailed logs and reports for each stage of execution?
yes, a detailed README.md explaining the projects and its features is necessary. Also, It is good to have a logging system at each step.


(1/10) - Can you clarify how the files in the project directory should be indexed? Should we use a specific database, vector embeddings, or file summaries stored in JSON?
Do whatever you think is the best.
(2/10) - For API key security in the `.env` file, should we assume any encryption standards or recommend specific tooling (e.g., dotenv parsers, encryption libraries)?
No. security is not needed for now.
(3/10) - Should any particular metadata schema or structure be followed for tasks assigned to the orchestrator and implementer agents? Beyond JSON format, are key fields standardized?
I don't know, do whatever you think is the best,
(4/10) - In terms of error management, beyond resetting branches, should the system log detailed error reports or implement retries with an incremental delay?
yes, that's a goot idea
(5/10) - Should the README.md include usage examples, or solely document updates and system functionality?
yes. include usage examples.
(6/10) - Are there any constraints or preferences for the programming libraries or frameworks to use for file indexing or integration beyond AzureOpenAI and LangChain (e.g., FAISS, ChromaDB)?
I don't know. do whatever you think is the best.
(7/10) - Do you foresee the need for modularity in agent design, allowing agents to be replaced or upgraded independently in the future?
yes. but for now, I want you to use AzureOpenAI LLMs with carefully designed prompts.
(8/10) - Should the logging mechanism output to both console and a file, and what level of verbosity (e.g., ERROR, INFO, DEBUG) is expected?
output only to a file. your verbosity suggestions are great.
(9/10) - For the system architecture, are there any additional integrations or third-party platforms to consider apart from AzureOpenAI and LangChain?
I don't know. do whatever you think is the best.
(10/10) - How should failures in AzureOpenAI API calls be handled if temporary issues arise? For instance, should we implement retries after a delay or fallback behaviors?
No, For know, just log it and exit the program.

    """

    develop_a_project("multi_agent", project_description)
