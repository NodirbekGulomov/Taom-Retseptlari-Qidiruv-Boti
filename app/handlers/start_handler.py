from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    text = (
        "Assalomu alaykum.\n\n"
        "Taom retseptini qidirish uchun:\n\n"
        "/taom nomini\n"
        "yoki\n"
        "/ingredient nomini\n\n"
        "yuboring."
    )
    await message.answer(text=text)
