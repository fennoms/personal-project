"""Helper functions for the auth routes."""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def validate_password(cls, password: str) -> str:
    """Validate the password field.

    If it is not provided, raise a ValueError.
    """
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long")

    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain at least one digit")

    if not any(char.isalpha() for char in password):
        raise ValueError("Password must contain at least one letter")

    return password


def validate_username(cls, username: str) -> str:
    """Validate the username field.

    If it is not provided, use the first part of the email address.
    """
    if len(username) < 3:
        raise ValueError("Username must be at least 3 characters long")
    return username


def hash_password(password: str) -> str:
    """Hash a password."""
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a password."""
    return pwd_context.verify(plain_password, hashed_password)
