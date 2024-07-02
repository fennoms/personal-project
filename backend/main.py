"""This file holds the main FastAPI application."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from db import init_db


@asynccontextmanager
def lifespan() -> None:
    """Perform startup and shutdown operations."""
    print("Application startup")
    init_db()
    yield
    print("Application shutdown")


app = FastAPI(
    docs_url="/api/docs",
    redoc_url=None,
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)
