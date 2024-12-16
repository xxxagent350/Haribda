import asyncio

from data_operators import db_operator
from variables.event_manager import text_event
from variables.bot import  dp
from aiogram import types
from variables.users_dict import users_dict
from models.user import User
from network import async_messages_operator

#Обработчик текста
@dp.message()
async def text_receiver(message: types.Message):
    chat_id = message.chat.id
    asyncio.create_task(async_messages_operator.try_delete_message(chat_id, message.message_id))
    if chat_id > 0:
        # Регаем игрока если ещё не зареган
        if not chat_id in users_dict:
            db_operator.add_user(chat_id)
            db_operator.try_get_user(5609117794)

        if not chat_id in users_dict.keys():
            User(chat_id)
        text_event.trigger(message = message)
    else:
        await message.bot.send_message(chat_id, "Недоступно в чатах")


