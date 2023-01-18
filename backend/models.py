"""Database models."""
from sqlalchemy import Boolean, Column, Integer, String, Identity

from database import Base


class Post(Base):
    """The posts table."""

    __tablename__ = "posts"
    id = Column(Integer, Identity(start=1), primary_key=True, index=True)
    username = Column(String)
    content = Column(String)
    like = Column(Boolean, nullable=True)
