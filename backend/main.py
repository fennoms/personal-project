"""Holds the main FastAPI application instance."""

from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import APIRouter, FastAPI

from db import init_db
from routers.auth.routes import router as auth_router
from routers.posts.routes import router as post_router


@asynccontextmanager
async def lifespan(app: FastAPI):
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

main_router = APIRouter(prefix="/api")
main_router.include_router(auth_router)
main_router.include_router(post_router)

app.include_router(main_router)
