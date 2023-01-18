"""Simple CRUD operations."""
from logging import getLogger

from sqlalchemy.orm import Session

import models
import schemas

LOGGER = getLogger(__name__)


def create_post(db: Session, post: schemas.ContentModel):
    """Create a post in the database"""
    LOGGER.info("Writing post %s", str(post))
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post_like(db: Session, response: schemas.ResponseModel):
    """Update a post with the user's response."""
    return db.query(models.Post).filter(models.Post.id == response.id).update({"like": response.like})
