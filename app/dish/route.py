from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from psycopg2.errors import UniqueViolation
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from .service import DishService
from .model import Dish, DishPost, DishUpdate, DishSerialize
from app.utils import get_error_code
from app.database import get_session

router = APIRouter()


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes")
async def get_dishes(
    menu_id: str,
    submenu_id: str,
    session: AsyncSession = Depends(get_session),
):
    try:
        dishes = await DishService.get_all_dishes(menu_id, submenu_id, session)
        fixed_dishes = [DishSerialize.from_post(dish) for dish in dishes]
        return fixed_dishes
    except Exception as error:
        raise HTTPException(
            status_code=get_error_code(error),
            detail=error.args[0],
        )


@router.get("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
async def get_dish(
    menu_id: str,
    submenu_id: str,
    dish_id: str,
    session: AsyncSession = Depends(get_session),
):
    try:
        dish = await DishService.get_dish(menu_id, submenu_id, dish_id, session)
        fixed_dish = DishSerialize.from_post(dish)
        return fixed_dish
    except Exception as error:
        raise HTTPException(
            status_code=get_error_code(error),
            detail=error.args[0],
        )


@router.post(
    "/menus/{menu_id}/submenus/{submenu_id}/dishes",
    status_code=201,
)
async def create_dish(
    menu_id: str,
    submenu_id: str,
    dish: DishPost,
    session: AsyncSession = Depends(get_session),
):
    try:
        dish = await DishService.create_dish(menu_id, submenu_id, dish, session)
        fixed_dish = DishSerialize.from_post(dish)
        return fixed_dish
    except Exception as error:
        raise HTTPException(
            status_code=get_error_code(error),
            detail=error.args[0],
        )


@router.patch("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
async def update_dish(
    menu_id: str,
    submenu_id: str,
    dish_id: str,
    dish: DishUpdate,
    session: AsyncSession = Depends(get_session),
):
    try:
        dish = await DishService.update_dish(
            menu_id, submenu_id, dish_id, dish, session
        )
        fixed_dish = DishSerialize.from_post(dish)
        return fixed_dish
    except Exception as error:
        raise HTTPException(
            status_code=get_error_code(error),
            detail=error.args[0],
        )


@router.delete("/menus/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
async def delete_dish(
    menu_id: str,
    submenu_id: str,
    dish_id: str,
    session: AsyncSession = Depends(get_session),
):
    try:
        return await DishService.delete_dish(menu_id, submenu_id, dish_id, session)
    except Exception as error:
        raise HTTPException(
            status_code=get_error_code(error),
            detail=error.args[0],
        )
