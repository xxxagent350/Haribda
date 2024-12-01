from variables.event_manager import call_event
from variables.bot import  dp
from core.user_list import user_list
from models.user import User

#Обработчик текста
@dp.callback_query()
async def text_receiver(message):
    if message.message.chat.id > 0:
        if not message.message.chat.id in user_list.keys():
            User(message.message.chat.id)
        call_event.trigger(message = message)
    else:
        await message.message.bot.send_message(message.message.chat.id, "Недоступнов чатах")
