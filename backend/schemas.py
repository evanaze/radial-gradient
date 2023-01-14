"""Schema for the backend objects."""
from pydantic import BaseModel


class ResponseModel(BaseModel):
    """The model of a response from the user."""

    id: str
    like: bool | None = None


class PostModel(ResponseModel):
    content: str

    class Config:
        orm_mode = True
