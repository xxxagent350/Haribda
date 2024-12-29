import asyncio

from aiogram import types
from aiogram.types import Message

from variables.bot import bot
from variables.maps_dict import maps
from models.action import Action,ActionType
from variables.users_dict import users_dict
from network import async_messages_operator


async def arrows_reaction(message: types.CallbackQuery):
    """
    Обработчик передвижения корабля игрока
    """
    match message.data:
        case "↑": # Верх
            maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, 0))
        case "←": # Влево
            maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, 90))
        case "→": # Вправо
            maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, -90))
        case "↓": # Вниз
           maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, 180))
        case "⬈": # Вправо вверх
            maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, -45))
        case "⬉": # Влево вверх
            maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, 45))
        case "⬋": # Влево вниз
            maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, 135))
        case "⬊": # Вправо вниз
            maps[0].add_new_delayed_action(Action(users_dict[message.message.chat.id].controlled_ship, ActionType.move, -135))
        case "bad_move_dir": # Движение в этом направлении невозможно
            sent_message: Message = await bot.send_message(message.message.chat.id, "Эта ячейка уже занята")
            asyncio.create_task(async_messages_operator.try_delete_message(message.message.chat.id, sent_message.message_id, 5))
