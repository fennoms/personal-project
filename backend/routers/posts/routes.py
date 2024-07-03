"""API endpoints for the /post route."""

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from db import get_session
from dependencies import get_current_user
from routers.posts.models import Post, PostBase
from routers.user.models import User

router = APIRouter(prefix="/post", tags=["post"])


@router.get("/")
def get_posts(
    session: Session = Depends(get_session), _: User = Depends(get_current_user)
) -> list[Post]:
    """Get all posts."""
    return session.exec(select(Post)).all()


@router.get("/{post_id}")
def get_post(
    post_id: int,
    session: Session = Depends(get_session),
    _: User = Depends(get_current_user),
) -> Post:
    """Get a single post."""
    post = session.get(Post, post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    return post


@router.post("/")
def create_post(
    post: PostBase,
    session: Session = Depends(get_session),
    _: User = Depends(get_current_user),
) -> Post:
    """Create a new post."""
    post = Post(**post.dict())
    session.add(post)
    session.commit()
    session.refresh(post)

    return post
