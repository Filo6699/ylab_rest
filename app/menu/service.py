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

        # query = select(Menu)
        # result = await session.execute(query)
        # for r in result:
        #     print(r)
        # serializable_result = [
        #     SearchResultMenu(
        #         id=menu.id,
        #         title=menu.title,
        #         description=menu.description,
        #         submenus_count=menu.submenus_count,
        #         dishes_count=menu.dishes_count,
        #     )
        #     for menu in result
        # ]
        # return serializable_result

    # @staticmethod
    # def get_menu_with_id(db: AsyncSession, id: uuid.uuid4):
    #     query = select(Menu.title, Menu.description).where(Menu.id == id)
    #     result = db.execute(query)
    #     return result

    @staticmethod
    async def create_menu(menu: MenuPost, session: AsyncSession) -> Menu:
        print(menu.id)
        new_menu = Menu(
            id=menu.id,
            title=menu.title,
            description=menu.description,
        )
        session.add(new_menu)
        await session.commit()
        await session.refresh(new_menu)
        return new_menu
