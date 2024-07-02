"""Models for the auth router."""

from pydantic import BaseModel


class Token(BaseModel):
    """Base class for a token."""

    access_token: str
    type: str


class TokenData(BaseModel):
    """Base class for token data."""

    id: int
