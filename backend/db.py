"""Holds the database configuration and session creation functions.

The get_session() function can be used with dependency injection to
inject API endpoints with a database session. The init_db() function
can be called on application startup to generate the database tables.
"""

import os
from dotenv import load_dotenv

from sqlmodel import Session, SQLModel, create_engine


load_dotenv()

# The database URL is found in the .env file stored under POSTGRES_URL
DATABASE_URL = os.getenv("POSTGRES_URL")
engine = create_engine(DATABASE_URL, echo=True)


def init_db() -> None:
    """Generate database tables."""
    SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    """Create a database session."""
    with Session(engine) as session:
        yield session
