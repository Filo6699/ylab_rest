from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .service import SubmenuService
from .model import SubmenuPost
from app.database import get_session

router = APIRouter()


@router.get("/menus/{menu_id}/submenus")
async def read_submenus(menu_id: str, session: AsyncSession = Depends(get_session)):
    print(type(menu_id))
    response = await SubmenuService.get_all_submenus(menu_id, session)
    return response


@router.post(
    "/menus/{menu_id}/submenus",
    status_code=201,
)
async def create_submenu(
    menu_id: str,
    submenu: SubmenuPost,
    session: AsyncSession = Depends(get_session),
):
    try:
        return await SubmenuService.create_submenu(menu_id, submenu, session)
    except Exception as error:
        if isinstance(error, HTTPException):
            raise error
        else:
            raise HTTPException(
                status_code=400,
                detail=error.args[0],
            )
