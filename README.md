# Project

I have started this simple project to learn about [FastAPI](https://fastapi.tiangolo.com/). I have used Flask before, but FastAPI has been growing in popularity, which is why I wanted to give it a try. The main features of this project are:

-   Login and registration using FastAPI and SQLModel
-   CI/CD Using GitHub actions and docker-compose
-   Simple frontend to call these API endpoints

NOTE: This project will not be finished, as it was purely for learning purposes, to learn about the development process using FastAPI.

# Installation

## Dependencies

### Backend

-   Docker and docker-compose [(Get Docker)](https://docs.docker.com/get-docker/).
-   Poetry [(Docs)](https://python-poetry.org/) It is recommended to use some sort of [virtual environment](https://docs.python.org/3/library/venv.html).

## Backend

### Run locally

After installing the dependencies, the command `fastapi run` can be used to run the development server.
NOTE: This does not create a database instance that can be used.

### Run using docker

The command `docker-compose build` followed by `docker-compose up` will spin up two containers; the FastAPI backend on port 8000, and the PostgreSQL database on port `POSTGRES_PORT` which must be configured as an environment variable.

### Environment variables

#### Frontend

Create a `.env` file inside of the frontend folder. It must contain the following:

```
NEXT_PUBLIC_API_URL=<api_url>
```

This environment variable is used to rewrite all calls of `/api/<path>` to `NEXT_PUBLIC_API_URL/<path>`. If developing locally, it can be set to `http://localhost:8000/api`. All requests made to `/api/<path>` in the frontend will be rewritten to that URL.

#### Backend

Create a `.env` file inside of the backend folder. It must contain the following:

```
POSTGRES_HOST=<postgres_host>
POSTGRES_PORT=<postgres_port>
POSTGRES_USER=<username>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<table_name>
POSTGRES_URL=postgresql://<username>:<password>@<postgres_host>:<postgres_port>/<table_name>
JWT_KEY=<jwt_key>
REDIS_PORT=<redis_port>
REDIS_URL=redis://<redis_host>:<redis_port>
```

If you use the `docker-compose` method, the `<postgres_host>` can be replaced with `db`, since Docker creates its own network where we can use the names of containers as hostnames. The same holds `<redis_host>`, which can be replaced by `redis`. A JWT key can be generated using `openssl rand -hex 16`.
