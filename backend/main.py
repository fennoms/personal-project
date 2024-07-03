"""Holds the main FastAPI application instance."""

import os
from contextlib import asynccontextmanager
from math import ceil

import redis.asyncio as redis
from dotenv import load_dotenv
from fastapi import (
    APIRouter,
    Depends,
    FastAPI,
    HTTPException,
    Request,
    Response,
    status,
)
from fastapi_limiter import FastAPILimiter
from fastapi_limiter.depends import RateLimiter

from db import init_db
from routers.auth.routes import router as auth_router
from routers.posts.routes import router as post_router


async def custom_callback(request: Request, response: Response, pexpire: int):
    """Create custom callback for rate limiting.

    Args:
    ----
        request (Request): Request object
        response (Response): Response object
        pexpire (int): Time in seconds until the rate limit expires

    Raises:
    ------
        HTTPException: Too Many Requests

    """
    expire = ceil(pexpire / 1000)

    raise HTTPException(
        status.HTTP_429_TOO_MANY_REQUESTS,
        f"Too Many Requests. Retry after {expire} seconds.",
        headers={"Retry-After": str(expire)},
    )


async def service_name_identifier(request: Request):
    """Identify the service name from the request headers.

    Args:
    ----
        request (Request): Request object

    Returns:
    -------
        _type_: str: Service name

    """
    service = request.headers.get("Service-Name")
    return service


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Create database tables on application startup."""
    print("Application startup")
    load_dotenv()
    init_db()
    redis_connection = redis.from_url(os.getenv("REDIS_URL"), encoding="utf8")
    await FastAPILimiter.init(
        redis=redis_connection,
        identifier=service_name_identifier,
        http_callback=custom_callback,
    )
    yield
    print("Application shutdown")
    await FastAPILimiter.close()


app = FastAPI(
    docs_url="/api/docs",
    redoc_url=None,
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

main_router = APIRouter(
    prefix="/api", dependencies=[Depends(RateLimiter(times=2, seconds=5))]
)
main_router.include_router(auth_router)
main_router.include_router(post_router)

app.include_router(main_router)
