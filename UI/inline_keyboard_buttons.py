from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from core.vector2 import Vector2
from variables.maps_dict import maps


def get_ship_control_buttons(user):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [get_ship_move_button(user, Vector2(-1, 1)), get_ship_move_button(user, Vector2(0, 1)), get_ship_move_button(user, Vector2(1, 1))],
            [get_ship_move_button(user, Vector2(-1, 0)), InlineKeyboardButton(text="🔵", callback_data="🔵"), get_ship_move_button(user, Vector2(1, 0))],
            [get_ship_move_button(user, Vector2(-1, -1)), get_ship_move_button(user, Vector2(0, -1)), get_ship_move_button(user, Vector2(1, -1))],
        ]
    )


def get_ship_move_button(user, delta_position):
    if maps[user.current_map_num].check_if_square_is_free(user.controlled_ship.position.summ(delta_position)):
        if delta_position.x == -1:
            if delta_position.y == 1:
                return InlineKeyboardButton(text="⬉", callback_data="⬉")
            if delta_position.y == 0:
                return InlineKeyboardButton(text="←", callback_data="←")
            if delta_position.y == -1:
                return InlineKeyboardButton(text="⬋", callback_data="⬋")
        if delta_position.x == 0:
            if delta_position.y == 1:
                return InlineKeyboardButton(text="↑", callback_data="↑")
            if delta_position.y == -1:
                return InlineKeyboardButton(text="↓", callback_data="↓")
        if delta_position.x == 1:
            if delta_position.y == 1:
                return InlineKeyboardButton(text="⬈", callback_data="⬈")
            if delta_position.y == 0:
                return InlineKeyboardButton(text="→", callback_data="→")
            if delta_position.y == -1:
                return InlineKeyboardButton(text="⬊", callback_data="⬊")
    else:
        return InlineKeyboardButton(text="🚫", callback_data="bad_move_dir")


cancel_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Отмена 🚫", callback_data="cancel")]
    ]
)


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