from aiogram import types
from UI.inline_keyboard_buttons import button_controller

async def command_map(message: types.Message):
    """
    Обработчик текстовой кнопки Карта🗺
    """

    # Проверяем, что команда "/start"
    if message.text == "Карта🗺":
        caption = "Карта"

        photo = types.FSInputFile("image.jpg")

        # Отправляем фото с текстом и кнопками
        await message.bot.send_photo(
                    chat_id=message.chat.id,
                    photo=photo,
                    caption=caption,
                    reply_markup = button_controller
                )

