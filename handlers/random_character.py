from aiogram import Router
from aiogram.types import CallbackQuery

from services.rick_morty_api import RickMortyAPI

router = Router()
api = RickMortyAPI()


@router.callback_query(lambda c: c.data == "random")
async def random_character(callback: CallbackQuery):
    await callback.answer()
    character = await api.get_random_character()
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
        parse_mode="HTML"
    )