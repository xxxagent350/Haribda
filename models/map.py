import asyncio
import copy

from UI import map_visualizer
from models.user import User
from models.world_objects.ship import Ship


class Map:
    def __init__(self):
        self.objects = []
        self.delayed_actions = [] # Действия, находящиеся в списке ожидания (передвижение корабля/существа, ныряние, постройка и т. д.)
        self.short_delayed_actions = []  # Короткие действия, находящиеся в списке ожидания (полёт снаряда, взрыв и т. д.)
        self.changed_squares = [] # Квадраты, на которых в были зафиксированы изменения(если такой квадрат находиться в поле видимости у игрока, то стоит перевыслать ему изображение карты)

    def add_new_object(self, object_):
        self.objects.append(object_)
        self.add_changed_square(object_)

    def add_new_delayed_action(self, new_action, short_action = False, override = True):
        """
        Добавляет ожидаемое действие в список действий на карте
        :param new_action: Сюда подавать экземпляр класса Action
        :param short_action: Короткое ли это действие
        :param override: Да = перезапишет запланированное действие этого объекта если уже есть другое, нет = добавит ещё одно в любом
        """
        # Обновляем сообщение карты, чтобы добавить кнопку Отмена
        if not short_action and type(new_action.object_) == Ship and type(new_action.object_.owner) == User:
            asyncio.create_task(map_visualizer.update_map_message_of_user(new_action.object_.owner, True))
            pass


        if not short_action:
            actions_list = self.delayed_actions
        else:
            actions_list = self.short_delayed_actions

        if override:
            actions_list = [action for action in actions_list if action.object_ != new_action.object_]
        actions_list.append(new_action)

        if not short_action:
            self.delayed_actions = actions_list
        else:
            self.short_delayed_actions = actions_list

    def check_if_object_has_delayed_actions(self, object_, short_actions = False):
        """Проверяет есть ли у объекта ожидаемые действия. Полезно для проверки есть ли уже у корабля действия в списке ожиданий, чтобы он не мог совершить более 1 действия за ход"""
        if not short_actions:
            delayed_actions_list = self.delayed_actions
        else:
            delayed_actions_list = self.short_delayed_actions

        for delayed_action in delayed_actions_list:
            if delayed_action.object_ == object_:
                return True
        return False

    def cancel_object_delayed_actions(self, object_):
        """Удаляет все отложенные действия объекта (кроме short actions, их отменить нельзя)"""
        self.delayed_actions = [action for action in self.delayed_actions if action.object_ != object_]

    def add_changed_square(self, object_):
        self.changed_squares.append(copy.deepcopy(object_.position))
