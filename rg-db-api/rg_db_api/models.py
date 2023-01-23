"""Database models."""
from sqlalchemy import Column, Integer, String, Identity, ForeignKey

from rg_db_api.database import Base


class Post(Base):
    """The posts table."""

    __tablename__ = "posts"
    id = Column(Integer, Identity(start=1), primary_key=True, index=True)
    author = Column(String)
    content = Column(String)


class User(Base):
    """The user table."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)


class Like(Base):
    """The likes table."""

    __tablename__ = "likes"
    id = Column(Integer, Identity(start=1), primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    post_id = Column(Integer, ForeignKey("posts.id"), nullable=False)
    like = Column(Integer, nullable=False)
