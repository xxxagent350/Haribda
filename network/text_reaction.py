from variables.event_manager import text_event
from variables.bot import  dp
from aiogram.filters import Command
from aiogram import types

#Обработчик текста
@dp.message()
async def text_receiver(message: types.Message):
    if message.chat.id > 0:
        text_event.trigger(message=message)
    else:
        await message.bot.send_message(message.chat.id, "Недоступнов чатах")


