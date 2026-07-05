from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="🎲 Случайный персонаж", callback_data="random")],
        [InlineKeyboardButton(text="🔍 Поиск по имени", callback_data="search")],
        [InlineKeyboardButton(text="📋 По статусу", callback_data="categories")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def back_to_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="Главное меню", callback_data="main_menu")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)