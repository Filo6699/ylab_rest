import uuid

from fastapi import Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from .model import Menu, MenuPost
from app.database import get_session


class MenuService:
    @staticmethod
    async def get_all_menus(session: AsyncSession = Depends(get_session)):
        return (await session.execute(select(Menu))).scalars().fetchall()

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
