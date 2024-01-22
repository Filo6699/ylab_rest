from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm.exc import NoResultFound

from .model import Dish, DishPost, DishUpdate
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
        dish = (await session.execute(query)).scalars().first()
        if not dish:
            raise NoResultFound("dish not found")
        return dish

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

    @staticmethod
    async def update_dish(
        menu_id: str,
        submenu_id: str,
        dish_id: str,
        dish_update: DishUpdate,
        session: AsyncSession,
    ) -> Dish:
        dish = await DishService.get_dish(menu_id, submenu_id, dish_id, session)
        if dish_update.title:
            dish.title = dish_update.title
        if dish_update.description:
            dish.description = dish_update.description
        if dish_update.price:
            dish.price = dish_update.price
        await session.merge(dish)
        await session.commit()
        await session.refresh(dish)
        return dish

    @staticmethod
    async def delete_dish(
        menu_id: str,
        submenu_id: str,
        dish_id: str,
        session: AsyncSession,
    ) -> None:
        dish = await DishService.get_dish(menu_id, submenu_id, dish_id, session)
        await session.delete(dish)
        await session.commit()
