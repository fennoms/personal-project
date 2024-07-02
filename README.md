# Project


# Installation

## Dependencies

### Backend
- Docker and docker-compose [(Get Docker)](https://docs.docker.com/get-docker/).
- Poetry [(Docs)](https://python-poetry.org/) It is recommended to use some sort of [virtual environment](https://docs.python.org/3/library/venv.html).

## Backend

### Run locally
After installing the  dependencies, the command `fastapi run` can be used to run the development server.
NOTE: This does not create a database instance that can be used.

### Run using docker
The command `docker-compose build` followed by `docker-compose up` will spin up two containers; the FastAPI backend on port 8000, and the PostgreSQL database on port `POSTGRES_PORT` which must be configured as an environment variable.

### Environment variables
Create a `.env` file inside of the backend folder. It must contain the following:

```
POSTGRES_URL=postgresql://<username>:<password>@<host>:<port>/<table_name>
```
If you use the `docker-compose` method, the `<host>` can be replaced with `db`, since Docker creates its own network where we can use the names of containers as hostnames.
