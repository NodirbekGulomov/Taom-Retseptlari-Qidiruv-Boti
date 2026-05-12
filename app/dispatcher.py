from aiogram import Dispatcher

from app.handlers.search_handlers import router as search_router
from app.handlers.start_handler import router as start_router

dp = Dispatcher()
dp.include_router(router=start_router)
dp.include_router(router=search_router)
