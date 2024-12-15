import asyncio

from variables.event_manager import text_event
from variables.bot import  dp
from aiogram import types
from variables.users_dict import users_dict
from models.user import User
from network import async_messages_operator

#Обработчик текста
@dp.message()
async def text_receiver(message: types.Message):
    asyncio.create_task(async_messages_operator.try_delete_message(message.chat.id, message.message_id))
    if message.chat.id > 0:
        if not message.chat.id in users_dict.keys():
            User(message.chat.id)
        text_event.trigger(message = message)
    else:
        await message.bot.send_message(message.chat.id, "Недоступно в чатах")


