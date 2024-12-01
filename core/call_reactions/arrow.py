from aiogram import types
from UI.inline_keyboard_buttons import button_controller
from core.map_list import maps
from core.action import Action,ActionType
from core.user_list import user_list



async def arrow(message: types.CallbackQuery):
    global maps
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
        print(user_list)
        maps[0].add_new_delayed_action(Action(user_list[message.message.chat.id].controlled_ship,0,180))




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
