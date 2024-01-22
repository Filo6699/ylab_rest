import uuid
from typing import List, Optional

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    relationship,
)
from pydantic import BaseModel, UUID4

from app.database import Base


class Menu(Base):
    __tablename__ = "menus"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    title = Column(String)
    description = Column(String)
    submenus = relationship("Submenu", back_populates="menu", cascade="all, delete")


class MenuPost(BaseModel):
    title: str
    description: str


class MenuUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
