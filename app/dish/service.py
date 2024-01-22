import uuid
from typing import List

from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from .model import Dish, DishPost
from app.database import get_session
from app.utils import convert_to_UUID


class DishService:
    @staticmethod
    async def get_all_dishes(
        menu_id: str,
        submenu_id: str,
        session: AsyncSession,
    ) -> List[Dish]:
        _ = convert_to_UUID(menu_id)
        submenu_id = convert_to_UUID(submenu_id)
        query = select(Dish).where(Dish.submenu_id == submenu_id)
        return (await session.execute(query)).scalars().fetchall()

    @staticmethod
    async def get_dish(
        menu_id: str,
        submenu_id: str,
        dish_id: str,
        session: AsyncSession,
    ) -> Dish:
        _ = convert_to_UUID(menu_id)
        submenu_id = convert_to_UUID(submenu_id)
        dish_id = convert_to_UUID(dish_id)
        query = select(Dish).where(
            Dish.submenu_id == submenu_id,
            Dish.id == dish_id,
        )
        return (await session.execute(query)).scalars().first()

    @staticmethod
    async def create_dish(
        menu_id: str,
        submenu_id: str,
        dish: DishPost,
        session: AsyncSession,
    ) -> Dish:
        _ = convert_to_UUID(menu_id)
        submenu_id = convert_to_UUID(submenu_id)
        new_dish = Dish(
            submenu_id=submenu_id,
            title=dish.title,
            description=dish.description,
            price=dish.price,
        )
        session.add(new_dish)
        await session.commit()
        await session.refresh(new_dish)
        return new_dish
