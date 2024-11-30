from variables.event_manager import call_event
from variables.bot import  dp

#Обработчик текста
@dp.callback_query()
async def text_receiver(message):
    if message.chat.id > 0:
        call_event.trigger(message = message)
    else:
        await message.bot.send_message(message.chat.id, "Недоступнов чатах")
