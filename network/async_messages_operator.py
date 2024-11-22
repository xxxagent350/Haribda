from variables.bot import bot
import asyncio
from aiogram.types import Message, InputMediaPhoto
import random
from core import images_operator


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

'''async def test_edit():
    message_id = 0
    while True:
        await asyncio.sleep(1)
        result, new_message_id = await try_strong_edit_message_media(5609117794,
                                                               message_id,
                                                               f"Абобус {random.randint(0, 100)}",
                                                               images_operator.get_image_from_ship_name(f"ship {random.randint(1, 5)}"),
                                                               max_edit_wait_time=1)
        if result:
            message_id = new_message_id
        else:
            print("Завершение")
            break'''

async def try_strong_edit_message_media(
    chat_id,
    message_id,
    new_caption=None,
    new_photo=None,
    new_reply_markup=None,
    max_edit_wait_time=1
) -> (bool, int):
    try:
        # Запускаем редактирование сообщения
        task = asyncio.create_task(
            bot.edit_message_media(
                chat_id=chat_id,
                message_id=message_id,
                media=InputMediaPhoto(media=new_photo, caption=new_caption),
                reply_markup=new_reply_markup
            )
        )

        # Ждем завершения редактирования в пределах max_edit_wait_time
        done, pending = await asyncio.wait([task], timeout=max_edit_wait_time)

        # Если задача завершилась
        try:
            if task in done:
                await task  # Проверяем на исключения
                print("Успешно изменено")
                return True, message_id
        except:
            pass

        # Если задача не завершилась, отменяем ее и обрабатываем
        for pending_task in pending:
            pending_task.cancel()

        print("Не удалось изменить сообщение, перевысылаю...")

        # Удаляем старое сообщение
        try:
            asyncio.create_task(try_delete_message(chat_id=chat_id, message_id=message_id))
        except:
            pass
        
        # Отправляем новое сообщение
        new_message: Message = await bot.send_photo(
            chat_id=chat_id,
            photo=new_photo,
            caption=new_caption,
            reply_markup=new_reply_markup
        )
        print("Перевыслано успешно")
        return True, new_message.message_id

    except NotImplementedError as exception:
        print(f"$ Warning - message's {message_id} in chat {chat_id} could not be edited or replaced: {exception}")
        return False, None
