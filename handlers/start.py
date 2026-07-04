from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from keyboards.main_menu import main_menu

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\nЯ бот по вселенной Rick & Morty\n\nВыбери что тебя интересует:",
        reply_markup=main_menu()
    )