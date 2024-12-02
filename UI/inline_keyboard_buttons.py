from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


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