from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from psycopg2.errors import UniqueViolation
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from .service import DishService
from .model import Dish
from app.utils import get_error_code
from app.database import get_session

router = APIRouter()

...
