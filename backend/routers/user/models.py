"""Models for users."""

from pydantic import EmailStr, field_validator
from sqlmodel import Field, SQLModel

from routers.auth.utils import validate_password, validate_username


class UserBase(SQLModel):
    """Base class for a user."""

    username: str = Field(sa_column_kwargs={"unique": True})

    @field_validator("username")
    def validate_username(cls, username: str):
        """Validate the username field."""
        return validate_username(cls, username)


class UserCreateRequest(UserBase):
    """Request body for creating a new user."""

    email: EmailStr = Field(sa_column_kwargs={"unique": True})
    password: str

    @field_validator("password")
    def validate_password(cls, password: str):
        """Validate the password field."""
        return validate_password(cls, password)


class UserLoginRequest(UserBase):
    """Request body for logging in a user."""

    email: EmailStr = Field(sa_column_kwargs={"unique": True})
    password: str

    @field_validator("password")
    def validate_password(cls, password: str):
        """Validate the password field."""
        return validate_password(cls, password)


class UserResponse(UserBase):
    """Response body for a user."""

    id: int


class User(UserBase, table=True):
    """Table schema for a user."""

    id: int = Field(default=None, primary_key=True)
    email: EmailStr = Field(sa_column_kwargs={"unique": True})
    password: str

    @field_validator("username")
    def validate_username(cls, username: str):
        """Validate the username field."""
        return validate_username(cls, username)

    @field_validator("password")
    def validate_password(cls, password: str):
        """Validate the password field."""
        return validate_password(cls, password)
