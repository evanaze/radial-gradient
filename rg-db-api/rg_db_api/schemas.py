"""Schema for the backend objects."""
from pydantic import BaseModel


class UserModel(BaseModel):
    id: int


class LikeModel(BaseModel):
    id: int
    user_id: int
    post_id: int
    like: bool | None = None


class ResponseModel(LikeModel):
    """The model of a response from the user."""

    id: str


class ContentModel(LikeModel):
    username: str
    content: str


class PostModel(ContentModel):
    id: str
    author: str

    class Config:
        orm_mode = True
