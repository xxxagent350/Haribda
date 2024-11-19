from variables.event_meneger import text_event
from variables.bot import  dp

#Обработчик текста
@dp.message()
async def text_receiver(message):
    text_event.trigger(message = message)


