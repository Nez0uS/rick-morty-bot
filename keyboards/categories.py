from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def categories_menu() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton(text="🟢 Живые", callback_data="status:alive")],
        [InlineKeyboardButton(text="🔴 Мёртвые", callback_data="status:dead")],
        [InlineKeyboardButton(text="⚪️ Неизвестные", callback_data="status:unknown")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)