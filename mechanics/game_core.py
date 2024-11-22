import asyncio

from models.world_objects.map import Map
from core.action import ActionType


maps = []
game_active = True
short_step_delay = 1 # Период обновления быстрых явлений(полёт снаряда, эффект взрыва и т. д.)
step_delay = 5 # Стандартный период обновления(передвижения корабля, совершение погружения и т. д.); ДОЛЖЕН БЫТЬ КРАТНЫМ short_step_delay !!!


def add_map():
    maps.append(Map)


async def process_game():
    global maps
    maps = [Map]

    while game_active:
        for map_ in maps:
            await asyncio.sleep(step_delay)
            process_map_iteration(map_)


def process_map_iteration(map_):
    for delayed_action in map_.delayed_actions:
        action_type = delayed_action.action_type
        if action_type == ActionType.move:
            print("move")
