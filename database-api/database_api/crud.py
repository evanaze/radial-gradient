"""Simple CRUD operations."""
import logging

from sqlalchemy.orm import Session

from database_api import models, schemas

logging.basicConfig(level="DEBUG")


def create_post(db: Session, post: schemas.ContentModel):
    """Create a post in the database"""
    logging.info("Writing post %s", str(post))
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def read_post(db: Session, content_id: str):
    """Read a post from the database.

    :param db: The database session.
    :param content_id: The post to read from the database.
    """
    query = db.query(models.Post).filter(models.Post.id == content_id)
    post = db.scalars(query).all()[0]
    logging.info("Post: %s", post)
    return post


def update_post_like(db: Session, content_id: str, like: schemas.LikeModel):
    """Update a post with the user's response.

    :param content_id: The ID of the content to update.
    :param like: The like value to set. Either True or False.
    """
    return db.query(models.Post).filter(models.Post.id == content_id).update({"like": like.like})
