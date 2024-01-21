import uuid

from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from .model import Dish, DishPost
from app.database import get_session


class DishService:
    ...
