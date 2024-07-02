"""This file holds the main FastAPI application."""

from fastapi import FastAPI

app = FastAPI(
    docs_url="/api/docs",
    redoc_url=None,
    openapi_url="/api/openapi.json",
)
