import asyncio
import random

from core.vector2 import Vector2
from core.action import ActionType, Action

# Импорт объектов карты
from models.world_objects.map import Map
from models.world_objects.ship import Ship
from models.world_objects.island import Island


maps = []
game_active = True
short_step_delay = 1 # Период обновления быстрых явлений(полёт снаряда, эффект взрыва и т. д.)
step_delay = 5 # Стандартный период обновления(передвижения корабля, совершение погружения и т. д.); ДОЛЖЕН БЫТЬ КРАТНЫМ short_step_delay !!!


def add_map(map_):
    maps.append(map_)


async def process_game():
    global maps

    test_map = Map()
    test_ship = Ship(sprite_name=f"ship {random.randint(1, 5)}", position=Vector2(2, 5), rotation=90, max_hp=100)
    test_action = Action(object_=test_ship, action_type=ActionType.move, value=0)
    test_map.delayed_actions.append(test_action)

    test_map.objects.append(test_action)
    maps = []
    add_map(test_map)

    while game_active:
        await asyncio.sleep(step_delay)
        for map_ in maps:
            process_map_iteration(map_)


def process_map_iteration(map_):
    for delayed_action in map_.delayed_actions:
        object_ = delayed_action.object_
        action_type = delayed_action.action_type

        if action_type == ActionType.move:
            map_.add_changed_square(object_)
            if type(object_) == Ship:
                match delayed_action.value:
                    case 0: # Вверх
                        object_.position.move(Vector2(0, 1))

        # Удаляем это действие из списка ожидаемых действий, так как только что выполнили его
        map_.delayed_actions.remove(delayed_action)
        print(map_.delayed_actions)
        map_.add_changed_square(object_)
        print(map_.delayed_actions)
