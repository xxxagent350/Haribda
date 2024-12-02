import asyncio, os

from aiogram.enums import ParseMode

from variables.bot import bot
from models.user import User
from UI.keyboard_buttons import button_map

from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def command_start(message: types.Message):
    """
    Обработчик команды /start.
    """
    #print('t', message.text, message.text == "/start")

    # Проверяем, что команда "/start"
    if message.text == "/start":
        caption = '''Добро пожаловать в мир Харибды! 🌊

Мир поглощён океаном, монстры держат остатки человечества в страхе, а вы – капитан корабля, который должен выжить и помочь восстановить цивилизацию. 🚢

- Управляйте своим кораблём.
- Исследуйте затонувшие города.
- Сражайтесь с монстрами и пиратами.
- Помните: одна ошибка – и всё потеряно.
⚓ Нажми *Карта* 🗺, чтобы начать своё путешествие:

Удачи, капитан! Только вы можете изменить судьбу человечества. 🌌'''

        photo = types.FSInputFile("sprites/intro_image.webp")

        # Отправляем фото с текстом и кнопками
        await message.bot.send_photo(
                    chat_id=message.chat.id,
                    photo=photo,
                    caption=caption,
                    parse_mode=ParseMode.MARKDOWN,
                    reply_markup = button_map
                )

