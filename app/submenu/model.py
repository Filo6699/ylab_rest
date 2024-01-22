import uuid
from typing import Optional

from sqlalchemy import Column, String, ForeignKey, select, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    column_property,
    relationship,
)
from pydantic import BaseModel

from app.database import Base
from app.dish.model import Dish


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
    dishes_count = column_property(
        select(func.count(Dish.id))
        .where(Dish.submenu_id == id)
        .correlate_except(Dish)
        .as_scalar()
    )


class SubmenuPost(BaseModel):
    title: str
    description: str


class SubmenuUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
