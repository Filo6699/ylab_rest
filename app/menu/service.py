import uuid

from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from .model import Menu, MenuPost, MenuUpdate
from app.database import get_session
from app.utils import convert_to_UUID


class MenuService:
    @staticmethod
    async def get_all_menus(session: AsyncSession = Depends(get_session)):
        return (await session.execute(select(Menu))).scalars().fetchall()

    @staticmethod
    async def get_menu(
        menu_id: str, session: AsyncSession = Depends(get_session)
    ) -> Menu:
        menu_id = convert_to_UUID(menu_id)
        query = select(Menu).where(Menu.id == menu_id)
        menu = (await session.execute(query)).scalars().first()
        if not menu:
            raise NoResultFound("menu not found")
        return menu

    @staticmethod
    async def create_menu(menu: MenuPost, session: AsyncSession) -> Menu:
        new_menu = Menu(
            title=menu.title,
            description=menu.description,
        )
        session.add(new_menu)
        await session.commit()
        await session.refresh(new_menu)
        return new_menu

    @staticmethod
    async def update_menu(
        menu_id: str, new_menu: MenuUpdate, session: AsyncSession
    ) -> Menu:
        menu = await MenuService.get_menu(menu_id, session)
        if new_menu.title:
            menu.title = new_menu.title
        if new_menu.description:
            menu.description = new_menu.description
        await session.merge(menu)
        await session.commit()
        await session.refresh(menu)
        return menu

    @staticmethod
    async def delete_menu(menu_id: str, session: AsyncSession):
        menu = await MenuService.get_menu(menu_id, session)
        await session.delete(menu)
        await session.commit()
