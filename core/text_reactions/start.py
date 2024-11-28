import asyncio, os
from variables.bot import bot
from models.user import User

from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def command_start(message: types.Message):
    """
    Обработчик команды /start.
    """
    print('t', message.text, message.text == "/start")

    # Проверяем, что команда "/start"
    if message.text == "/start":
        caption = "Вот пример изображения с кнопками."

        # Создаём клавиатуру с кнопками
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text = "Кнопка 1", callback_data="button1"),
                    InlineKeyboardButton(text = "Кнопка 2", callback_data="button2"),
                    InlineKeyboardButton(text = "Кнопка 3", callback_data="button3"),
                ],
                [
                    InlineKeyboardButton(text = "Кнопка 4", callback_data="button4"),
                    InlineKeyboardButton(text = "Кнопка 5", callback_data="button5"),
                    InlineKeyboardButton(text = "Кнопка 6", callback_data="button6"),
                ],
                [
                    InlineKeyboardButton(text = "Кнопка 7", callback_data="button7"),
                    InlineKeyboardButton(text = "Кнопка 8", callback_data="button8"),
                    InlineKeyboardButton(text = "Кнопка 9", callback_data="button9"),
                ]
            ]
        )

        # URL изображения
        #photo_url = "https://static.wikia.nocookie.net/mushokutensei/images/7/75/ErisAnime1.png/revision/latest/scale-to-width/360?cb=20230516191642"  # Замените на актуальный путь к файлу или ссылку
        photo = types.FSInputFile("image.jpg")
        # Отправляем фото с текстом и кнопками
        await message.bot.send_photo(
                    chat_id=message.chat.id,
                    photo=photo,
                    caption=caption,
                    reply_markup=keyboard
                )

