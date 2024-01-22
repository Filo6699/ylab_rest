from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from psycopg2.errors import UniqueViolation
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from .service import MenuService
from .model import MenuPost, MenuUpdate
from app.database import get_session
from app.utils import get_error_code

router = APIRouter()


@router.get("/menus")
async def get_all_menus(response=Depends(MenuService.get_all_menus)):
    return response


@router.get("/menus/{menu_id}")
async def get_menu(menu_id: str, session: AsyncSession = Depends(get_session)):
    try:
        return await MenuService.get_menu(menu_id, session)
    except Exception as error:
        raise HTTPException(
            status_code=get_error_code(error),
            detail=error.args[0],
        )


@router.post(
    "/menus",
    status_code=201,
)
async def post_new_menu(menu: MenuPost, session: AsyncSession = Depends(get_session)):
    try:
        return await MenuService.create_menu(menu=menu, session=session)
    except Exception as error:
        raise HTTPException(
            status_code=get_error_code(error),
            detail=error.args[0],
        )


@router.patch("/menus/{menu_id}")
async def patch_menu(
    menu_id: str,
    menu: MenuUpdate,
    session: AsyncSession = Depends(get_session),
):
    try:
        return await MenuService.update_menu(menu_id, menu, session)
    except Exception as error:
        raise HTTPException(
            status_code=get_error_code(error),
            detail=error.args[0],
        )


@router.delete("/menus/{menu_id}")
async def delete_menu(
    menu_id: str,
    session: AsyncSession = Depends(get_session),
):
    try:
        return await MenuService.delete_menu(menu_id, session)
    except Exception as error:
        raise HTTPException(
            status_code=get_error_code(error),
            detail=error.args[0],
        )
