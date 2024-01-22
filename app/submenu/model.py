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
from pydantic import BaseModel

from app.database import Base


class Submenu(Base):
    __tablename__ = "submenus"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    menu_id = Column(UUID, ForeignKey("menus.id"), index=True)
    title = Column(String)
    description = Column(String)
    menu = relationship("Menu", back_populates="submenus")
    dishes = relationship("Dish", back_populates="submenu", cascade="all, delete")


class SubmenuPost(BaseModel):
    title: str
    description: str


class SubmenuUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
