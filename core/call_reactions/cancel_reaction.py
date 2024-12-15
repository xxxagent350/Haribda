import asyncio

from aiogram import types

from variables.maps_dict import maps
from variables.users_dict import users_dict
from UI import map_visualizer


async def cancel_reaction(message: types.CallbackQuery):
    """Обработчик кнопки отмены хода"""
    if message.data == "cancel":
        if message.message.chat.id in users_dict and users_dict[message.message.chat.id].current_map is not None and users_dict[message.message.chat.id].controlled_ship is not None:
            maps[users_dict[message.message.chat.id].current_map].cancel_object_delayed_actions(users_dict[message.message.chat.id].controlled_ship)
            asyncio.create_task(map_visualizer.update_map_message_of_user(users_dict[message.message.chat.id], True))
