"""Routes for authentication."""

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session, select

from db import get_session
from dependencies import create_access_token, get_current_user
from routers.auth.models import Token
from routers.auth.utils import hash_password, verify_password
from routers.user.models import User, UserCreateRequest, UserResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register", response_model=Token)
async def register(
    user: UserCreateRequest, session: Session = Depends(get_session)
) -> Token:
    """Register a new user."""
    try:
        new_user = User(
            username=user.username,
            email=user.email,
            password=hash_password(user.password),
        )
        session.add(new_user)
        session.commit()
        session.refresh(new_user)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="User already exists")

    token = create_access_token({"id": new_user.id})

    return Token(access_token=token, type="bearer")


@router.post("/login", response_model=Token)
async def login(
    user: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)
) -> Token:
    """Login a user."""
    user_db = session.exec(select(User).filter(User.username == user.username)).first()

    if user_db is None:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(user.password, user_db.password):
        raise HTTPException(status_code=404, detail="Incorrect password")

    token = create_access_token({"id": user_db.id})

    return Token(access_token=token, type="bearer")


@router.get("/verify")
def get_current_user(user: UserResponse = Depends(get_current_user)) -> UserResponse:
    """Get the current user."""
    return user
