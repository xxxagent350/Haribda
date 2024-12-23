import asyncio
import math
import time
from random import randint

from models.world_objects.monster import Monster
from variables.maps_dict import maps
from core.vector2 import Vector2
from core.action import ActionType, Action
from UI.map_visualizer import update_map_message_of_user

# Импорт объектов карты
from models.user import User
from models.world_objects.ship import Ship
from models.world_objects.debris import Debris

from settings.global_settings import render_out_of_border_range

game_active = True
short_step_delay = 1 # Период обновления быстрых явлений(полёт снаряда, эффект взрыва и т. д.)
step_delay = 3 # Стандартный период обновления(передвижения корабля, совершение погружения и т. д.); ДОЛЖЕН БЫТЬ КРАТНЫМ short_step_delay !!!


# Запускает автоматическое совершение запланированных действие с заданным интервалом
async def process_game():
    if step_delay % short_step_delay != 0:
        raise Exception("$ Невозможно запустить game_core.process_game, так как step_delay не кратен short_step_delay, а это условие обязательно")

    short_step_num = 0
    short_steps_in_basic_step = int(step_delay / short_step_delay) # Раз в сколько быстрых обновлений делать стандартное обновление
    while game_active:
        await asyncio.sleep(short_step_delay)
        for map_ in maps.values():
            try:
                process_delayed_actions_on_map(map_, True)
                process_monsters_attack_on_map(map_)
                short_step_num += 1
                if short_step_num >= short_steps_in_basic_step:
                    process_ai_on_map(map_)
                    process_delayed_actions_on_map(map_, False)
                    short_step_num = 0
                update_visual_map(map_)
            except Exception as exception:
                print(f'Непредвиденная критическая ошибка в game_core.process_game: {exception}')


# Логика ботов
def process_ai_on_map(map_):
    for monster in map_.objects:
        try:
            if type(monster) == Monster:
                monster.process_monster_logics(map_)
        except Exception as exception:
            print(f'Непредвиденная ошибка в game_core.process_ai_on_map: {exception}')


def process_monsters_attack_on_map(map_):
    for monster in map_.objects:
        try:
            if type(monster) == Monster:
                monster.attack()
        except Exception as exception:
            print(f'Непредвиденная ошибка в game_core.process_monsters_on_map: {exception}')


# Совершение запланированных действий
def process_delayed_actions_on_map(map_, short_update):
    if not short_update:
        delayed_actions_list = map_.delayed_actions
    else:
        delayed_actions_list = map_.short_delayed_actions

    delayed_actions_to_remove = []
    for delayed_action in delayed_actions_list:
        try:
            object_ = delayed_action.object_
            action_type = delayed_action.action_type
            action_succeed = False
            if action_type == ActionType.move:
                # Обработчик движения
                map_.add_changed_square(object_)
                if type(delayed_action.value) == Vector2:
                    action_succeed = object_.try_move_with_delta(delayed_action.value, map_)
                else:
                    action_succeed = object_.try_move_at_dir(delayed_action.value, map_)

            # Добавляем действие в список на удаление
            delayed_actions_to_remove.append(delayed_action)

            # Помечаем также квадрат на котором стоит объект сейчас на случай если он сдвинулся
            if action_succeed:
                map_.add_changed_square(object_)
        except Exception as exception:
            print(f'Непредвиденная ошибка в game_core.process_map_iteration: {exception}')
            delayed_actions_to_remove.append(delayed_action)

    # Удаляем выполненные запланированные действия
    if short_update:
        for action_to_remove in delayed_actions_to_remove:
            map_.short_delayed_actions = [action for action in map_.short_delayed_actions if not action == action_to_remove]
    else:
        for action_to_remove in delayed_actions_to_remove:
            map_.delayed_actions = [action for action in map_.delayed_actions if not action == action_to_remove]


# Обновление визуальных карт у игроков, которым это необходимо
def update_visual_map(map_):
    showed_changed_squares = dict() # Сюда добавляем квадраты на карте, которые уже были "погашены", то есть игроки их увидели
    users_to_update_map = dict()
    for i,object_ in enumerate(map_.objects):
        if type(object_) == Debris:
            if object_.decrement_lifetime():
                map_.objects.pop(i)
        if type(object_) == Ship:
            if not object_.life_check():
                map_.objects.append(Debris(object_.position,0,"debris", 3))
                map_.objects.pop(i)
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
        asyncio.create_task(update_map_message_of_user(user))

    # Удаляем "погашенные" квадраты из списка
    for showed_changed_square in showed_changed_squares.keys():
        map_.changed_squares = [changed_square for changed_square in map_.changed_squares if not changed_square.equals(showed_changed_square)]
