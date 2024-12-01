from variables.event_manager import text_event
from variables.bot import  dp
from aiogram.filters import Command
from aiogram import types
from core.user_list import user_list
from models.user import User

#Обработчик текста
@dp.message()
async def text_receiver(message: types.Message):
    if message.chat.id > 0:
        if not message.chat.id in user_list.keys():
            User(message.chat.id)
        text_event.trigger(message=message)
    else:
        await message.bot.send_message(message.chat.id, "Недоступнов чатах")


