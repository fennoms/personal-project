"""Routes for authentication."""

from fastapi import APIRouter, Depends
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from db import get_session
from dependencies import create_access_token
from routers.user.models import User, UserCreateRequest, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
async def register(user: UserCreateRequest, session: Session = Depends(get_session)):
    """Register a new user."""
    try:
        new_user = User(
            username=user.username, email=user.email, password=user.password
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    except IntegrityError:
        return {"error": "Username or email already exists"}

    token = create_access_token({"id": new_user.id})

    return UserResponse(username=new_user.username, id=new_user.id, token=token)
