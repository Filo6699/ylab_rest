from uuid import UUID

from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .model import Submenu, SubmenuPost
from app.database import convert_to_UUID


class SubmenuService:
    @staticmethod
    async def get_all_submenus(menu_id: str, session: AsyncSession):
        menu_id = convert_to_UUID(menu_id)
        query = select(Submenu).where(Submenu.menu_id == menu_id)
        return (await session.execute(query)).scalars().fetchall()

    @staticmethod
    async def get_submenu(menu_id: str, submenu_id: str, session: AsyncSession):
        menu_id = convert_to_UUID(menu_id)
        submenu_id = convert_to_UUID(submenu_id)
        query = select(Submenu).where(
            Submenu.menu_id == menu_id,
            Submenu.id == submenu_id,
        )
        return (await session.execute(query)).scalars().fetchall()

    @staticmethod
    async def create_submenu(menu_id: str, submenu: SubmenuPost, session: AsyncSession):
        menu_id = convert_to_UUID(menu_id)
        new_submenu = Submenu(
            menu_id=menu_id,
            title=submenu.title,
            description=submenu.description,
        )
        session.add(new_submenu)
        await session.commit()
        await session.refresh(new_submenu)
        return new_submenu
