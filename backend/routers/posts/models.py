"""Models for the post router."""

from sqlmodel import Field, SQLModel


class PostBase(SQLModel):
    """Base class for Post model."""

    title: str
    content: str


class Post(PostBase, table=True):
    """Post model, which is a table in the database."""

    id: int = Field(default=None, primary_key=True)
