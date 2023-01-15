"""Database models."""
from sqlalchemy import Boolean, Column, Integer, String

from database import Base


class Posts(Base):
    """The posts table."""

    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    liked = Column(Boolean, nullable=True)
