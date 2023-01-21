"""Simple CRUD operations."""
from sqlalchemy.orm import Session

from database_api import models, schemas


def create_post(db: Session, post: schemas.PostModel):
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


def read_post(db: Session, content_id: str):
    """Read a post from the database.

    :param db: The database session.
    :param content_id: The post to read from the database.
    """
    query = db.query(models.Post).filter(models.Post.id == content_id)
    return db.scalars(query).all()[0]


def update_post_like(db: Session, content_id: str, like: schemas.LikeModel):
    """Update a post with the user's response.

    :param content_id: The ID of the content to update.
    :param like: The like value to set. Either True or False.
    """
    return (
        db.query(models.Post)
        .filter(models.Post.id == content_id)
        .update({"like": like.like})
    )
