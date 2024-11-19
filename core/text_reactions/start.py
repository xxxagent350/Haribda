import asyncio
from variables.bot import bot

async def command_start(message = None):
    print('t',message.text,message.text == "/start")
    if message.text == "/start":
        await bot.send_message(message.chat.id, "Hellow, world!")
