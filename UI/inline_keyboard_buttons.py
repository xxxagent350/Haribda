from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

button_controller = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="⬉", callback_data="⬉"),InlineKeyboardButton(text="🢁", callback_data="🢁"),InlineKeyboardButton(text="⬈", callback_data="⬈")],
        [InlineKeyboardButton(text="🢀", callback_data="🢀"),InlineKeyboardButton(text="🔵", callback_data="🔵"),InlineKeyboardButton(text="🢂", callback_data="🢂")],
        [InlineKeyboardButton(text="⬋", callback_data="⬋"),InlineKeyboardButton(text="🢃", callback_data="🢃"),InlineKeyboardButton(text="⬊", callback_data="⬊")],
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