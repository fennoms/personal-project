"""Models for users."""

from sqlmodel import Field, SQLModel
from typing import Optional
from pydantic import field_validator, EmailStr


class UserBase(SQLModel):
    """Base class for a user."""

    username: Optional[str] = None


class UserCreateRequest(UserBase):
    """Request body for creating a new user."""

    email: EmailStr
    password: str


class UserLoginRequest(UserBase):
    """Request body for logging in a user."""

    email: EmailStr
    password: str


class UserResponse(UserBase):
    """Response body for a user."""

    id: int


class User(UserBase, table=True):
    """Table schema for a user."""

    id: int = Field(default=None, primary_key=True)
    username: str = Field(sa_column_kwargs={"unique": True})
    email: EmailStr
    password: str

    @field_validator("username")
    def validate_username(cls, values):
        """Validate the username field.

        If it is not provided, use the first part of the email address.
        """
        if not values.get("username"):
            values["username"] = values["email"].split("@")[0]
        return values

    @field_validator("password")
    def validate_password(cls, values):
        """Validate the password field.

        If it is not provided, raise a ValueError.
        """
        if not values.get("password"):
            raise ValueError("Password is required")

        password = values["password"]

        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long")

        if not any(char.isdigit() for char in password):
            raise ValueError("Password must contain at least one digit")

        if not any(char.isalpha() for char in password):
            raise ValueError("Password must contain at least one letter")

        return values
