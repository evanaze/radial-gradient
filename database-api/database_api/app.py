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


@app.post("/create_post")
def create_post(post: schemas.PostModel, db: Session = Depends(get_db)):
    """Create a post in the database."""
    return crud.create_post(db, post)


@app.post("/response")
def record_response(post: schemas.ResponseModel, db: Session = Depends(get_db)):
    """Record a response to the database."""
    return crud.update_post_like(db, post)
