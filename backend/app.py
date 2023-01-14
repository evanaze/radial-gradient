from fastapi import FastAPI

from backend import schemas, crud

app = FastAPI()


@app.post("/response")
def record_response(response: schemas.ResponseModel):
    """Record a response to the database."""
    return crud.update_post_like(response)
