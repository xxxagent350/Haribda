from random import randint

from aiogram import types
from UI.inline_keyboard_buttons import button_controller
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
        if user_.controlled_ship is None:
            player_ship = Ship(position=Vector2(randint(-2, 2), randint(-2, 2)), rotation=0, sprite_name=f'ship {randint(1, 5)}')
            player_ship.register_owner(user_)
            maps[0].add_new_object(player_ship)


            '''caption = "Это карта"

            photo = types.FSInputFile("image.jpg")

            # Отправляем фото с текстом и кнопками
            await message.bot.send_photo(
                        chat_id=message.chat.id,
                        photo=photo,
                        caption=caption,
                        reply_markup = button_controller
                    )'''

