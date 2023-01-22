"""Simple CRUD operations."""
from sqlalchemy import select
from sqlalchemy.orm import Session

from rg_db_api import models, schemas


def create_post(db: Session, post: schemas.PostModel) -> schemas.PostResponseModel:
    """Create a post in the database"""
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def create_like(db: Session, like: schemas.LikeModel):
    """Create a like in the database."""
    db_like = models.Like(**like.dict())
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like


def read_likes(db: Session) -> list[dict]:
    """Read all of the likes from the database.

    :param db: The database session.
    """
    query = db.query(models.Like)
    return db.scalars(query).all()


def read_post(db: Session, content_id: str):
    """Read a post from the database.

    :param db: The database session.
    :param content_id: The post to read from the database.
    """
    posts = models.Post
    query = select(models.Post).where(posts.id == content_id)
    return db.execute(query).fetchone()
