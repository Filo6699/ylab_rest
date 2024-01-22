import uuid
from typing import List, Optional

from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    relationship,
)
from pydantic import BaseModel, validator

from app.database import Base


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    submenu_id = Column(UUID, ForeignKey("submenus.id"), index=True)
    submenu = relationship("Submenu", back_populates="dishes")
    title = Column(String)
    description = Column(String)
    price = Column(DECIMAL(scale=2))


class DishPost(BaseModel):
    title: str
    description: str
    price: str

    @validator("price")
    def validate_float(cls, value: str) -> float:
        num = float(value)
        fnum = "{:.2f}".format(num)
        if value == fnum:
            return num
        raise ValueError("Price number should have precision of 2 numbers.")


class DishUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[str] = None

    @validator("price")
    def validate_float(cls, value: str) -> float:
        num = float(value)
        fnum = "{:.2f}".format(num)
        if value == fnum:
            return num
        raise ValueError("Price number should have precision of 2 numbers.")


class DishSerialize(BaseModel):
    id: uuid.UUID
    submenu_id: uuid.UUID
    title: str
    description: str
    price: str

    @staticmethod
    def from_post(dish: Dish):
        return DishSerialize(
            id=dish.id,
            submenu_id=dish.submenu_id,
            title=dish.title,
            description=dish.description,
            price="{:.2f}".format(dish.price),
        )
