from variables.event_manager import text_event
from variables.bot import  dp

#Обработчик текста
@dp.message_handler(content_types=["text"])
async def text_receiver(message):
    print(message)
    text_event.trigger(message = message)


