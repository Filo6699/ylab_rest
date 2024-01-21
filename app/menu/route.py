from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from psycopg2.errors import UniqueViolation
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from .service import MenuService
from .model import MenuPost
from app.database import get_session

router = APIRouter()


@router.get("/menus")
async def get_all_menus(response=Depends(MenuService.get_all_menus)):
    return response


@router.post(
    "/menus",
    status_code=201,
)
async def post_new_menu(menu: MenuPost, session: AsyncSession = Depends(get_session)):
    try:
        return await MenuService.create_menu(menu=menu, session=session)
    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=error.args[0],
        )
