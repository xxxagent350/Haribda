import asyncio
from variables.bot import bot
from models.user import User

async def command_start(message = None):
    print('t',message.text,message.text == "/start")
    if message.text == "/start":
        await bot.send_message(message.chat.id, "Hellow, world!")
        User(message.chat.id)
