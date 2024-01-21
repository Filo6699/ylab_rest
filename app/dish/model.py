import uuid
from typing import List

from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    relationship,
)
from pydantic import BaseModel

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
    ...
