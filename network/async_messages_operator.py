from variables.bot import bot
import asyncio
from aiogram.types import Message, InputMediaPhoto
import random
from core import images_operator


async def try_delete_message(chat_id, message_id, delay = 0) -> bool:
    """
    :param chat_id: ID чата, в котором хотите удалить сообщение
    :param message_id: ID сообщения, которое хотите удалить
    :param delay: задержка перед удалением сообщения в секундах
    :return: успех операции
    """
    await asyncio.sleep(delay)
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
    new_caption=None,
    new_photo=None,
    new_reply_markup=None,
    max_edit_wait_time=1
) -> (bool, int):
    """
    Изменяет сообщение, при неудаче пытается удалить сообщение с message_id и выслать новое(в таком случае вернёт id нового сообщения, иначе - изменённого)
    :param chat_id: id чата
    :param message_id: id сообщения
    :param new_caption: новая подпись
    :param new_photo: новое фото
    :param new_reply_markup: новый reply_markup
    :param max_edit_wait_time: максимальное время ожидания изменения сообщения(при превышении перевышлется)
    :return: удачно ли изменено, id изменённого сообщения(оно могло измениться)
    """
    try:
        # Запускаем редактирование сообщения
        if new_photo is not None:
            task = asyncio.create_task(
                bot.edit_message_media(
                    chat_id=chat_id,
                    message_id=message_id,
                    media=InputMediaPhoto(media=new_photo, caption=new_caption),
                    reply_markup=new_reply_markup
                )
            )
        else:
            task = asyncio.create_task(
                bot.edit_message_caption(
                    chat_id=chat_id,
                    message_id=message_id,
                    caption=new_caption,
                    reply_markup=new_reply_markup
                )
            )

        # Ждем завершения редактирования в пределах max_edit_wait_time
        done, pending = await asyncio.wait([task], timeout=max_edit_wait_time)

        # Если задача завершилась
        try:
            if task in done:
                await task  # Проверяем на исключения
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
        if new_photo is not None:
            new_message: Message = await bot.send_photo(
                chat_id=chat_id,
                photo=new_photo,
                caption=new_caption,
                reply_markup=new_reply_markup
            )
        else:
            return False, None

        print("Перевыслано успешно")
        return True, new_message.message_id

    except Exception as exception:
        print(f"$ Warning - message's {message_id} in chat {chat_id} could not be edited or replaced: {exception}")
        return False, None
