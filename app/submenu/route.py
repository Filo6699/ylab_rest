from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from .service import SubmenuService
from .model import SubmenuPost, SubmenuUpdate
from app.database import get_session

router = APIRouter()


@router.get("/menus/{menu_id}/submenus")
async def read_submenus(
    menu_id: str,
    session: AsyncSession = Depends(get_session),
):
    try:
        return await SubmenuService.get_all_submenus(menu_id, session)
    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=error.args[0],
        )


@router.get("/menus/{menu_id}/submenus/{submenu_id}")
async def read_submenus(
    menu_id: str,
    submenu_id: str,
    session: AsyncSession = Depends(get_session),
):
    try:
        return await SubmenuService.get_submenu(menu_id, submenu_id, session)
    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=error.args[0],
        )


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
        raise HTTPException(
            status_code=400,
            detail=error.args[0],
        )


@router.patch("/menus/{menu_id}/submenus/{submenu_id}")
async def patch_submenu(
    menu_id: str,
    submenu_id: str,
    submenu: SubmenuUpdate,
    session: AsyncSession = Depends(get_session),
):
    try:
        return await SubmenuService.update_submenu(menu_id, submenu_id, submenu, session)
    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=error.args[0],
        )
