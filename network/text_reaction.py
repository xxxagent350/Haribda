from variables.event_manager import text_event
from variables.bot import  dp
from aiogram.filters import Command
from aiogram import types

#Обработчик текста
@dp.message(Command("start"))
async def text_receiver(message: types.Message):
    text_event.trigger(message=message)


