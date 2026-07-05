from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from services.rick_morty_api import RickMortyAPI

router = Router()
api = RickMortyAPI()

class SearchStates(StatesGroup):
    waiting_for_name = State()
    

@router.callback_query(lambda c: c.data == "search")
async def search_start(callback: CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.set_state(SearchStates.waiting_for_name)
    await callback.message.answer("Введи имя персонажа, например: Rick, Morty, Beth")


@router.message(SearchStates.waiting_for_name)
async def search_result(message: Message, state: FSMContext):
    await state.clear()
    results = await api.search_by_name(message.text)

    if not results:
        await message.answer("Персонаж не найден 😔")
        return

    # 1. Создай пустую строку
    text = f"Найдено: {len(results)}\n\n"

    # 2. Пройдись по results циклом
    for i, character in enumerate(results[:10], start=1):
        # 3. Добавь к text строчку с номером, именем и статусом
        text += f"{i}: {character['name']} - {character['status']}\n"

    await message.answer(text)