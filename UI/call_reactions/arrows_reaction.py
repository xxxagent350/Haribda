from aiogram import types
from UI.inline_keyboard_buttons import button_controller
from core.map_list import maps
from core.action import Action,ActionType
from core.user_list import users_dict


async def arrow(message: types.CallbackQuery):
    """
    Обработчик стрелок передвижения
    """
    if message.data == "↑":
        # Верх
        maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, 0))

    elif message.data == "←":
        # Влево
        maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, 90))

    elif message.data == "→":
        # Вправо
        maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, -90))

    elif message.data == "↓":
        # Вниз
        maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, 180))

    elif message.data == "⬈":
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

    elif message.data == "⬋":
        # Левый нижний угол
        await message.message.bot.send_message(
            chat_id=message.message.chat.id,
            text="Стрелочка направлена в левый нижний угол"
        )

    elif message.data == "⬊":
        # Правый нижний угол
        await message.message.bot.send_message(
            chat_id=message.message.chat.id,
            text="Стрелочка направлена в правый нижний угол"
        )
