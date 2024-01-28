from fastapi import FastAPI

from app.menu.route import router as menu_router
from app.submenu.route import router as submenu_router
from app.dish.route import router as dish_router

app = FastAPI()

for router in [menu_router, submenu_router, dish_router]:
    app.include_router(router, prefix="/api/v1")
