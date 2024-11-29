from aiogram import types
from UI.inline_keyboard_buttons import button_controller

async def arrow(message: types.CallbackQuery):
    """
        Обработчик текстовых кнопок на клавиатуре
    """
    print(message.data)
    if message.data == "⬈":
        # Правый верхний угол
        await message.message.bot.send_message(
            chat_id=message.message.chat.id,
            text="Стрелочка направлена в правый верхний угол"
        )

    elif message.data == "⬉":
        # Левый верхний угол
        await message.message.bot.send_message(
            chat_id=message.message.chat.id,
            text="Стрелочка направлена в левый верхний угол"
        )

    elif message.data == "🢁":
        # Верх
        await message.message.bot.send_message(
            chat_id=message.message.chat.id,
            text="Стрелочка направлена вверх"
        )

    elif message.data == "🢀":
        # Влево
        await message.message.bot.send_message(
            chat_id=message.message.chat.id,
            text="Стрелочка направлена влево"
        )

    elif message.data == "🢂":
        # Вправо
        await message.message.bot.send_message(
            chat_id=message.message.chat.id,
            text="Стрелочка направлена вправо"
        )

    elif message.data == "⬋":
        # Левый нижний угол
        await message.message.bot.send_message(
            chat_id=message.message.chat.id,
            text="Стрелочка направлена в левый нижний угол"
        )

    elif message.data == "🢃":
        # Вниз
        await message.message.bot.send_message(
            chat_id=message.message.chat.id,
            text="Стрелочка направлена вниз"
        )

    elif message.data == "⬊":
        # Правый нижний угол
        await message.message.bot.send_message(
            chat_id=message.message.chat.id,
            text="Стрелочка направлена в правый нижний угол"
        )
