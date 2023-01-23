"""Schema for the backend objects."""
from pydantic import BaseModel


class ResponseModel(BaseModel):
    id: int


class UserModel(ResponseModel):
    class Config:
        orm_mode = True


class LikeModel(BaseModel):
    user_id: int
    post_id: int
    like: int


class LikeResponseModel(ResponseModel, LikeModel):
    class Config:
        orm_mode = True


class PostModel(BaseModel):
    author: str
    content: str


class PostResponseModel(PostModel, ResponseModel):
    class Config:
        orm_mode = True
