"""Routes for authentication."""

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from db import get_session
from dependencies import create_access_token
from routers.user.models import User, UserCreateRequest, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register", response_model=UserResponse)
async def register(
    user: UserCreateRequest, session: Session = Depends(get_session)
) -> UserResponse:
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


@router.post("/login", response_model=UserResponse)
async def login(
    user: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)
) -> UserResponse:
    """Login a user."""
    user = session.exec(select(User).filter(User.username == user.username)).first()

    if user is None:
        return {"error": "User not found"}

    if user.password != user.password:
        return {"error": "Invalid password"}

    token = create_access_token({"id": user.id})

    return UserResponse(username=user.username, id=user.id, token=token)
