from core.bot import bot

async def try_delete_message(chat_id, message_id):
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        return True
    except Exception as exception:
        print(f'Warning - message {message_id} in chat {chat_id} cannot be deleted: {exception}')
        return False


async def try_edit_message_text(chat_id, message_id, new_message_text):
    try:
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=new_message_text)
        return True
    except Exception as exception:
        print(f"Warning - message's {message_id} text in chat {chat_id} cannot be edited to '{new_message_text}': {exception}")
        return False

