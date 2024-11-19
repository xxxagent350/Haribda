from variables.bot import bot
import asyncio
from main import subscribe_on_start

@subscribe_on_start
def test1():
    print("Победоо")

async def try_delete_message(chat_id, message_id) -> bool:
    try:
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        return True
    except Exception as exception:
        print(f'$ Warning - message {message_id} in chat {chat_id} cannot be deleted: {exception}')
        return False


async def try_edit_message_text(chat_id, message_id, new_message_text) -> bool:
    try:
        await bot.edit_message_text(chat_id=chat_id, message_id=message_id, text=new_message_text)
        return True
    except Exception as exception:
        print(f"$ Warning - message's {message_id} text in chat {chat_id} cannot be edited to '{new_message_text}': {exception}")
        return False

async def try_strong_edit_message_media(
    chat_id,
    message_id,
    new_message_text,
    message_media,
    reply_markup=None,
    max_edit_wait_time=5
) -> bool:
    try:
        # Запускаем редактирование сообщения
        task = asyncio.create_task(
            bot.edit_message_media(
                chat_id=chat_id,
                message_id=message_id,
                text=new_message_text,
                media=message_media,
                reply_markup=reply_markup
            )
        )

        # Ждем завершения редактирования в пределах max_edit_wait_time
        done, pending = await asyncio.wait([task], timeout=max_edit_wait_time)

        # Если задача завершилась
        if task in done:
            await task  # Проверяем на исключения
            print("Успешно изменено")
            return True

        # Если задача не завершилась, отменяем ее и обрабатываем
        for pending_task in pending:
            pending_task.cancel()

        print("Не удалось изменить сообщение, перевысылаю...")

        # Удаляем старое сообщение
        await bot.delete_message(chat_id=chat_id, message_id=message_id)
        
        # Отправляем новое сообщение
        await bot.send_message(
            chat_id=chat_id,
            text=new_message_text,
            reply_markup=reply_markup
        )
        print("Перевыслано успешно")
        return True

    except Exception as exception:
        print(f"$ Warning - message's {message_id} in chat {chat_id} could not be edited or replaced: {exception}")
        return False
