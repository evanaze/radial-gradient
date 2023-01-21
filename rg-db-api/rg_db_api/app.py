"""The main app."""
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database_api import crud, schemas, models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/content", response_model=schemas.PostModel)
def create_post(post: schemas.ContentModel, db: Session = Depends(get_db)):
    """Create a post in the database."""
    return crud.create_post(db, post)


@app.post("/like", response_model=schemas.LikeResponseModel)
def create_like(like: schemas.LikeModel, db: Session = Depends(get_db)):
    """Create a like in the database."""
    return crud.create_like(db, like)


@app.get("/content/{content_id}", response_model=schemas.PostModel)
def read_post(content_id: str, db: Session = Depends(get_db)):
    """Read a post from the database"""
    return crud.read_post(db, content_id)


@app.put("/content/{content_id}", response_model=schemas.LikeModel)
def record_response(
    content_id: str, like: schemas.LikeModel, db: Session = Depends(get_db)
):
    """Record a response to the database."""
    return crud.update_post_like(db, content_id, like)
