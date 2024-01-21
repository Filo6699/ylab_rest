from uuid import UUID

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from .model import Submenu, SubmenuPost


class SubmenuService:
    ...


#     @staticmethod
#     def get_submenu(menu_id: UUID, submenu_id: UUID, db: Session):
#         query = select(Submenu.title, Submenu.description).where(
#             Submenu.id == submenu_id and Submenu.menu_id == menu_id
#         )
#         result = db.execute(query)
#         return result

#     @staticmethod
#     def get_submenus(menu_id: UUID, db: Session):
#         query = select(Submenu.title, Submenu.description).where(
#             Submenu.menu_id == menu_id
#         )
#         result = db.execute(query)
#         print(result)
#         return result

#     @staticmethod
#     def create_submenu(menu_id: UUID, submenu: SubmenuPost, db: Session):
#         if (
#             db.query(Submenu)
#             .filter(Submenu.menu_id == menu_id, Submenu.title == submenu.title)
#             .first()
#             is not None
#         ):
#             return {"ok": False, "error": "Submenu with that title already exists."}
#         new_submenu = Submenu(
#             menu_id=menu_id,
#             title=submenu.title,
#             description=submenu.description,
#         )
#         try:
#             db.add(new_submenu)
#             db.commit()
#         except Exception as err:
#             return {"ok": False, "error": err}
#         return {"ok": True, "id": str(new_submenu.id)}
