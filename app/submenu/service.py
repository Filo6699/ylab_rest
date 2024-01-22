from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .model import Submenu, SubmenuPost


class SubmenuService:
    @staticmethod
    async def get_all_submenus(menu_id, session: AsyncSession):
        menu_id = UUID(menu_id)
        query = select(Submenu).where(Submenu.menu_id == menu_id)
        return (await session.execute(query)).scalars().fetchall()

    @staticmethod
    async def create_submenu(menu_id, submenu: SubmenuPost, session: AsyncSession):
        try:
            menu_id = UUID(menu_id)
        except ValueError:
            raise ValueError("Некорретный формат UUID меню.")
        new_submenu = Submenu(
            menu_id=menu_id,
            title=submenu.title,
            description=submenu.description,
        )
        session.add(new_submenu)
        await session.commit()
        await session.refresh(new_submenu)
        return new_submenu
