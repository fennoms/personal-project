"""Models for the auth router."""

from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """Base class for a token."""

    token: Optional[str] = None
    type: str


class TokenData(BaseModel):
    """Base class for token data."""

    id: int
