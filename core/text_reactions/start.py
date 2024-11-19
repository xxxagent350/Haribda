import asyncio
from variables.bot import bot

async def command_start(message = None):
    if message.text == "/start":
        bot.send_message(message.chat.id, "Hellow, world!")
        #bot.send_dice(message.chat.id)
