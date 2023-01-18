"""Simple CRUD operations."""
from sqlalchemy.orm import Session

import models
import schemas


def create_post(db: Session, post: schemas.PostModel):
    """Create a post in the database"""
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post_like(db: Session, response: schemas.ResponseModel):
    """Update a post with the user's response."""
    return db.query(models.Post).filter(models.Post.id == response.id).update({"like": response.like})
