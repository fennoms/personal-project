"""This file holds the database connection and the logic to
create all tables in the database."""

import os

from sqlmodel import Session, SQLModel, create_engine

# The database URL is found in the .env file stored under POSTGRES_URL
DATABASE_URL = os.getenv("POSTGRES_URL")

engine = create_engine(DATABASE_URL, echo=True)


def init_db() -> None:
    """Generates database tables."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """Creates a database session."""
    with Session(engine) as session:
        yield session
