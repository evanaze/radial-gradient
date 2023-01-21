"""Schema for the backend objects."""
from pydantic import BaseModel


class LikeModel(BaseModel):
    like: bool | None = None


class ResponseModel(LikeModel):
    """The model of a response from the user."""

    id: str


class ContentModel(LikeModel):
    username: str
    content: str


class PostModel(ContentModel):
    id: str

    class Config:
        orm_mode = True
