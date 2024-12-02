from aiogram import types
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
        maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, -45))


    elif message.data == "⬉":
        # Левый верхний угол
        maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, 45))


    elif message.data == "⬋":
        # Левый нижний угол
        maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, 135))


    elif message.data == "⬊":
        # Правый нижний угол
        maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, -135))
