"""Simple CRUD operations."""
from sqlalchemy.orm import Session

import models, schemas


def update_post_like(db: Session, response: schemas.ResponseModel):
    """Update a post with the user's response."""
    return db.query(models.Posts).filter(models.Posts.id == response.id).update({"like": response.like})
