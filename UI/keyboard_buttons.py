from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_map = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="Нажми меня")]
            ],
            resize_keyboard=True  # Уменьшаем размер кнопки
        )