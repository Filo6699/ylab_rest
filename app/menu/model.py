import uuid
from typing import Optional

from sqlalchemy import Column, String, select, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    column_property,
    relationship,
)
from pydantic import BaseModel

from app.submenu.model import Submenu
from app.dish.model import Dish
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
    submenus_count = column_property(
        select(func.count(Submenu.id))
        .where(Submenu.menu_id == id)
        .correlate_except(Submenu)
        .as_scalar()
    )
    dishes_count = column_property(
        select(func.count(Dish.id))
        .where(Dish.submenu_id.in_(select(Submenu.id).where(Submenu.menu_id == id)))
        .correlate_except(Dish)
        .as_scalar()
    )


class MenuPost(BaseModel):
    title: str
    description: str


class MenuUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
