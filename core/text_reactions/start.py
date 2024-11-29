import asyncio, os
from variables.bot import bot
from models.user import User
from UI.keyboard_buttons import button_map

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def command_start(message: types.Message):
    """
    Обработчик команды /start.
    """
    print('t', message.text, message.text == "/start")

    # Проверяем, что команда "/start"
    if message.text == "/start":
        caption = "Добро пожалывать. Готов к погружению?"

        photo = types.FSInputFile("image.webp")

        # Отправляем фото с текстом и кнопками
        await message.bot.send_photo(
                    chat_id=message.chat.id,
                    photo=photo,
                    caption=caption,
                    reply_markup = button_map
                )

