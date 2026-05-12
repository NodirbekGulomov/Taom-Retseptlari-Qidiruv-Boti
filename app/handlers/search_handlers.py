from aiogram import Router, F
from aiogram.types import Message

from app.db.commands import search_by_taom, search_by_ingredient
from app.services.formater import format_retseptlar

router = Router()


@router.message(F.text.startswith("/taom"))
async def search_by_taom_handler(message: Message):
    if message.text:
        text = message.text.replace("/taom", "").strip()
        msg = format_retseptlar(search_by_taom(text))
        await message.answer(text=msg)


@router.message(F.text.startswith("/ingredient"))
async def search_by_ingredient_handler(message: Message):
    if message.text:
        text = message.text.replace("/ingredient", "").strip()
        msg = format_retseptlar(search_by_ingredient(text))
        await message.answer(text=msg)
