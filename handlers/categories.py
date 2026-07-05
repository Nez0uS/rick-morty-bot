from aiogram import Router
from aiogram.types import CallbackQuery
from keyboards.categories import categories_menu
from keyboards.main_menu import back_to_menu

from services.rick_morty_api import RickMortyAPI

api = RickMortyAPI()
router = Router()

@router.callback_query(lambda c: c.data == "categories")
async def show_categories(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer("Выбери статус:", reply_markup=categories_menu())


@router.callback_query(lambda c: c.data.startswith("status:"))
async def show_by_status(callback: CallbackQuery):
    await callback.answer()
    status = callback.data.split(":")[1]
    results = await api.get_by_status(status)
    character = results[0]
    text = (
        f"<b>{character['name']}</b>\n\n"
        f"Статус: {character['status']}\n"
        f"Вид: {character['species']}\n"
        f"Пол: {character['gender']}\n"
        f"Локация: {character['location']['name']}"
    )
    await callback.message.answer_photo(
        photo=character["image"],
        caption=text,
        parse_mode="HTML",
        reply_markup=back_to_menu()
    )