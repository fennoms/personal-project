"""Module containing the dependencies for the FastAPI application."""

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
import os
from datetime import datetime, timedelta
import jwt
from sqlmodel import Session
from db import get_session
from routers.auth.models import TokenData
from routers.user.models import UserResponse, User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")
JWT_KEY = os.getenv("JWT_KEY")


def create_access_token(data: dict, expires_delta: int = 60):
    """Create an access token with the given data."""
    expire = datetime.now() + timedelta(minutes=expires_delta)
    to_encode = data.copy()
    to_encode.update({"expire": expire.strftime("%Y-%m-%d %H:%M:%S")})

    return jwt.encode(to_encode, JWT_KEY, algorithm="HS256")


def verify_access_token(token: str) -> TokenData:
    """Verify the access token and return the token data."""
    try:
        payload = jwt.decode(token, JWT_KEY, algorithms=["HS256"])

        id: int = payload.get("id")

    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.InvalidTokenError:
        raise ValueError("Invalid token")

    return TokenData(id=id)


def get_current_user(
    token: str = Depends(oauth2_scheme), session: Session = Depends(get_session)
) -> UserResponse:
    """Get the current user from the access token."""
    token = verify_access_token(token)
    user = session.get(User, token.id)

    if user is None:
        raise ValueError("User not found")

    return UserResponse(username=user.username, id=user.id, token=token)
