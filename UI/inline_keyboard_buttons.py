from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from UI.keyboard_buttons import button_map
from core.map_list import maps


ship_control_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬉", callback_data="⬉"),InlineKeyboardButton(text="↑", callback_data="↑"),InlineKeyboardButton(text="⬈", callback_data="⬈")],
        [InlineKeyboardButton(text="←", callback_data="←"),InlineKeyboardButton(text="🔵", callback_data="🔵"),InlineKeyboardButton(text="→", callback_data="→")],
        [InlineKeyboardButton(text="⬋", callback_data="⬋"),InlineKeyboardButton(text="↓", callback_data="↓"),InlineKeyboardButton(text="⬊", callback_data="⬊")],
    ]
)

cancel_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отмена 🚫", callback_data="cancel")]
    ]
)

def get_ship_control_inline_keyboard(user):
    if not maps[user.current_map].check_if_object_has_delayed_actions(user.controlled_ship):
        buttons = ship_control_buttons
    else:
        buttons = cancel_button
    return buttons



"""Однотонные квадраты:
◼️ Черный квадрат
◻️ Белый квадрат
▪️ Маленький черный квадрат
▫️ Маленький белый квадрат
Цветные квадраты:
🔴 Красный квадрат
🟠 Оранжевый квадрат
🟡 Желтый квадрат
🟢 Зеленый квадрат
🔵 Синий квадрат
🟣 Фиолетовый квадрат
🟤 Коричневый квадрат
⚫ Черный (круглый) квадрат
⚪ Белый (круглый) квадрат
Границы:
⬛ Черный большой квадрат
⬜ Белый большой квадрат"""