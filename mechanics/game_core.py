import asyncio
import random

from aiogram.filters import and_f

from core.vector2 import Vector2
from core.action import ActionType, Action
from UI.map_visualizer import visualize_map_to_user

# Импорт объектов карты
from models.user import User
from models.world_objects.map import Map
from models.world_objects.ship import Ship
from models.world_objects.island import Island

from settings.global_settings import render_out_of_border_range


maps = []
game_active = True
short_step_delay = 1 # Период обновления быстрых явлений(полёт снаряда, эффект взрыва и т. д.)
step_delay = 5 # Стандартный период обновления(передвижения корабля, совершение погружения и т. д.); ДОЛЖЕН БЫТЬ КРАТНЫМ short_step_delay !!!


def add_map(map_):
    maps.append(map_)


# Запускает автоматическое совершение запланированных действие с заданным интервалом
async def process_game():
    if step_delay % short_step_delay != 0:
        raise Exception("$ Невозможно запустить game_core.process_game, так как step_delay не кратен short_step_delay, а это условие обязательно")
    global maps

    '''test_map = Map()
    test_user = User(5609117794)
    test_ship = Ship(owner=test_user, sprite_name=f"ship {2}", position=Vector2(2, 5), rotation=90, max_hp=100)
    test_ship2 = Ship(owner=test_user, sprite_name=f"ship {4}", position=Vector2(1, 2), rotation=180, max_hp=100)
    test_user.controlled_ship = test_ship
    test_user.current_map = test_map
    test_action = Action(object_=test_ship, action_type=ActionType.move, value=180)
    test_map.add_new_object(test_ship)
    test_map.add_new_object(test_ship2)
    test_map.add_new_delayed_action(test_action)
    maps = []
    add_map(test_map)'''

    short_step_num = 0
    short_steps_in_basic_step = int(step_delay / short_step_delay) # Раз в сколько быстрых обновлений делать стандартное обновление
    while game_active:
        await asyncio.sleep(short_step_delay)
        for map_ in maps:
            process_map_iteration(map_, True)
            short_step_num += 1
            if short_step_num >= short_steps_in_basic_step:
                process_map_iteration(map_, False)
                short_step_num = 0

            update_visual_map(map_)


# Совершение запланированных действий
def process_map_iteration(map_, short_update):
    if not short_update:
        delayed_actions_list = map_.delayed_actions
    else:
        delayed_actions_list = map_.short_delayed_actions

    for delayed_action in delayed_actions_list:
        object_ = delayed_action.object_
        action_type = delayed_action.action_type
        if action_type == ActionType.move:
            map_.add_changed_square(object_)
            if type(object_) == Ship:
                object_.move(delayed_action.value)

        # Удаляем это действие из списка ожидаемых действий, так как только что выполнили его
        map_.delayed_actions.remove(delayed_action)

        # Помечаем также квадрат на котором стоит объект сейчас на случай если он сдвинулся
        map_.add_changed_square(object_)


# Обновление визуальных карт у игроков, которым это необходимо
def update_visual_map(map_):
    showed_changed_squares = dict() # Сюда добавляем квадраты на карте, которые уже были "погашены", то есть игроки их увидели
    users_to_update_map = dict()
    for object_ in map_.objects:
        if type(object_) == Ship and type(object_.owner) == User:
            min_view_limits = object_.position.summ(Vector2(-object_.view_range - render_out_of_border_range, -object_.view_range - render_out_of_border_range))
            max_view_limits = object_.position.summ(Vector2(object_.view_range + render_out_of_border_range, object_.view_range + render_out_of_border_range))

            for changed_square in map_.changed_squares:
                # Проверка лежит ли изменённый квадрат в области видимости игрока
                if min_view_limits.x <= changed_square.x <= max_view_limits.x and min_view_limits.y <= changed_square.y <= max_view_limits.y:
                    showed_changed_squares[Vector2(changed_square.x, changed_square.y)] = True
                    users_to_update_map[object_.owner] = True

    # Отсылаем карты заново кому надо
    for user in users_to_update_map.keys():
        asyncio.create_task(visualize_map_to_user(map_, user))

    # Удаляем "погашенные" квадраты из списка
    for showed_changed_square in showed_changed_squares.keys():
        map_.changed_squares = [changed_square for changed_square in map_.changed_squares if not changed_square.equals(showed_changed_square)]
