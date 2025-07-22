from masds import build_project


if __name__ == "__main__":
    project_description = """
    I'm want you to build a database microservice using Nodejs.
    The microservice should run on a local server and it will be served using API calls.
    It should manage multiple databases. I want to add / remove / edit databases. check their health, find which one of them is fastest, and forward the user CRUD request to that database.

    (1/10) | What database management systems or types (e.g., MySQL, MongoDB, PostgreSQL) are we targeting?
All of the above.                                                                       (2/10) | What criteria should be used to determine which database is 'fastest'? (e.g., latency, throughput)
latency
(3/10) | What metrics define the health of a database, and how should these checks be conducted?
for now, check if the database is alive and responsive.
(4/10) | What kind of CRUD operations need to be supported, and should there be different APIs for each operation?
I will provide the CRUD operations later. Just create a placeholder for ORM and CRUD operations.
(5/10) | Should there be any user authentication or authorization for API calls? If so, what method (e.g., token-based)?
yes. bearer token is fine.
(6/10) | How should the system forward CRUD requests to the databases? Should it dynamically choose the fastest or allow the user to select a specific one?
Implement both options. "auto" for fastest.                                           o
(7/10) | Any specific response format or error-handling mechanism required for the APIs?
the response format should be in json
(8/10) | Do you need logging or monitoring for the microservice (e.g., for database performance or errors)?
yes, of course.
(9/10) | Should the service support scalability for future expansion, such as additional databases or distributed environments?
yes
(10/10) | Is there a preferred structure for database configurations (e.g., JSON, YAML file, or database)?
the database configs will be provided in a JSON file.
    """
    # mark 'is_clear' as true and fill all the missing information with whatever you think is the best.
    # """

    build_project("founderise", project_description)
