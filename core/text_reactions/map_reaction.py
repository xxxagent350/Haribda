import asyncio
from random import randint

from aiogram import types
from UI.inline_keyboard_buttons import ship_control_buttons
from UI.map_visualizer import update_map_message_of_user
from network import async_messages_operator
from core.vector2 import Vector2
from core.map_list import maps
from models import user
from models.world_objects.ship import Ship
import random

async def map_button_reaction(message: types.Message):
    """
    Обработчик текстовой кнопки Карта 🗺
    """
    # Проверяем команду
    if message.text == "Карта 🗺":
        # Получаем пользователя
        user_ = user.users_dict[message.chat.id]

        # Проверка есть ли у игрока корабль
        if user_.controlled_ship == 0:
            player_ship = Ship(position=Vector2(randint(-2, 2), randint(-2, 2)), rotation=0, sprite_name=f'ship {randint(1, 5)}')
            player_ship.register_owner(user_)
            maps[user_.current_map].add_new_object(player_ship)
        else:
            for i in maps:
                for object_ in i.objects:
                    if type(object_) == Ship:
                        if object_.owner.id == user_.id:
                            user_.controlled_ship  =  object_
                            break


        # Удаляем старую карту если она была и отсылаем новую
        asyncio.create_task(async_messages_operator.try_delete_message(user_.id, user_.map_message_id))
        user_.map_message_id = None
        asyncio.create_task(update_map_message_of_user(user_))
