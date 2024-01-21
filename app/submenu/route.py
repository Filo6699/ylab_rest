from uuid import UUID

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from psycopg2.errors import UniqueViolation
from sqlalchemy.orm import Session

from .service import SubmenuService
from .model import SubmenuPost
from app.database import get_session

router = APIRouter()


# don't ask questions.

# @router.get("/menus/{menu_id}/submenus")
# async def read_submenus(menu_id: UUID, db: Session = Depends(get_db)):
#     response_fields = []
#     for item in SubmenuService.get_submenus(menu_id, db):
#         response_fields.append(item)
#     return response_fields


# @router.get("/menus/{menu_id}/submenus/{submenu_id}")
# async def read_submenu(menu_id: UUID, submenu_id: UUID, db: Session = Depends(get_db)):
#     response_fields = []
#     for item in SubmenuService.get_submenu(menu_id, submenu_id, db):
#         response_fields.append(item)
#     return response_fields


# @router.post("/menus/{menu_id}/submenus")
# def create_submenu(
#     menu_id: UUID, submenu: SubmenuCreationModel, db: Session = Depends(get_db)
# ):
#     result = SubmenuService.create_submenu(menu_id, submenu, db)
#     if result["ok"] == False:
#         error = result["error"]
#         status_code = 400
#         response = {"message": error}
#         return JSONResponse(content=response, status_code=status_code)
#     else:
#         response = {
#             "title": submenu.title,
#             "description": submenu.description,
#             "id": result["id"],
#         }
#         return JSONResponse(content=response, status_code=201)
