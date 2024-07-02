"""Holds the main FastAPI application instance."""

from contextlib import asynccontextmanager

from db import init_db
from fastapi import FastAPI
from dotenv import load_dotenv


@asynccontextmanager
async def lifespan(app: FastAPI) -> None:
    """Create database tables on application startup."""
    print("Application startup")
    load_dotenv()
    init_db()
    yield
    print("Application shutdown")


app = FastAPI(
    docs_url="/api/docs",
    redoc_url=None,
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)
