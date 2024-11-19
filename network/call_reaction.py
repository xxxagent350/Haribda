from variables.event_manager import call_event
from variables.bot import  dp

#Обработчик текста
@dp.callback_query()
async def text_receiver(message):
    call_event.trigger(message = message)
