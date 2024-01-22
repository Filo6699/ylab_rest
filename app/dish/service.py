import uuid

from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from .model import Dish, DishPost
from app.database import get_session
from app.utils import convert_to_UUID


class DishService:
    ...
