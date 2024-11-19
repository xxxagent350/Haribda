import asyncio
from variables.bot import bot

def command_start(message = None):
    print('t',message.text,message.text == "/start")
    if message.text == "/start":
        bot.send_message(message.chat.id, "Hellow, world!")
        #bot.send_dice(message.chat.id)
