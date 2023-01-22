"""The main app."""
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from rg_db_api import crud, schemas, models, database

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/content", response_model=schemas.PostResponseModel)
def create_post(post: schemas.PostModel, db: Session = Depends(get_db)):
    """Create a post in the database."""
    return crud.create_post(db, post)


@app.post("/like", response_model=schemas.LikeResponseModel)
def create_like(like: schemas.LikeModel, db: Session = Depends(get_db)):
    """Create a like in the database."""
    return crud.create_like(db, like)


@app.get("/like", response_model=schemas.LikeResponseModel)
def read_likes(db: Session = Depends(get_db)):
    """Get all likes in the database."""
    return crud.read_likes(db)


@app.get("/content/{content_id}", response_model=schemas.PostResponseModel)
def read_post(content_id: str, db: Session = Depends(get_db)):
    """Read a post from the database"""
    return crud.read_post(db, content_id)
