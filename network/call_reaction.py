from variables.event_manager import call_event
from variables.bot import  dp
from models.user import User
from data_operators import db_operator
from variables.users_dict import users_dict

#Обработчик текста
@dp.callback_query()
async def text_receiver(message):
    chat_id = message.message.chat.id
    if chat_id > 0:
        # Регаем игрока если ещё не зареган
        if not chat_id in users_dict:
            db_operator.add_user(chat_id)

        if not chat_id in users_dict.keys():
            User(chat_id)
        call_event.trigger(message = message)
    else:
        await message.message.bot.send_message(chat_id, "Недоступно в чатах")
