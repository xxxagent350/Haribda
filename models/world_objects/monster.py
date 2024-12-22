import math

from core.action import ActionType, Action
from core.vector2 import Vector2
from models.world_objects.game_object import GameObject
from core import images_operator
from models.world_objects.ship import Ship


class Monster(GameObject):
    def __init__(self, position, rotation, sprite_name, max_hp, scale = 1, agr_range = 2, attack_range = 1, view_range = 3, freeze_rotation_at = None, updates_to_move = 1):
        """
        Монстр
        :param position: стартовая позиция
        :param rotation: стартовый поворот
        :param sprite_name: название спрайта
        :param max_hp: максимальное здоровье
        :param scale: масштаб картинки
        :param agr_range: радиус агра
        :param attack_range: радиус атаки (не менее 1)
        :param view_range: радиус видимости, при превышении перестанет преследовать цель
        :param freeze_rotation_at: укажите поворот изображения в градусах (None = автоматический поворот в сторону движения)
        :param updates_to_move: раз в сколько обновлений будет двигаться монстр (1 = со скоростью игрока, 2 = в 2 раза реже)
        """
        super().__init__(position, rotation, images_operator.get_image_path_from_monster_name(sprite_name), scale)
        self.max_hp = max_hp
        self.agr_range = agr_range
        self.freeze_rotation_at = freeze_rotation_at
        self.updates_to_move = updates_to_move
        self.view_range = view_range
        self.attack_range = attack_range

        self.target = None
        self.updates_num_from_last_move = 0

        if attack_range < 1:
            raise Exception(f'Ошибка при создании экземпляра класса Monster: attack_range менее 1 (ваше значение - {attack_range})')
        if type(updates_to_move) != int:
            raise Exception(f'Ошибка при создании экземпляра класса Monster: updates_to_move должен быть типа int, а он типа {type(updates_to_move)}')
        if updates_to_move < 1:
            raise Exception(f'Ошибка при создании экземпляра класса Monster: updates_to_move должен быть более 0 (ваше значение - {updates_to_move})')


    # Логика ботов
    def process_monster_logics(self, map_):
        try:
            # Определение цели монстра
            nearest_target = None
            nearest_distance = self.agr_range + 999
            for target in map_.objects:
                if type(target) == Ship:
                    distance = math.sqrt((self.position.x - target.position.x) ** 2 + (self.position.y - target.position.y) ** 2)
                    if distance < self.agr_range + 0.5 and :
                        self.target = target

            if self.target is not None:
                # Проверка не убежала ли цель из зоны видимости
                distance = math.sqrt((self.position.x - self.target.position.x) ** 2 + (self.position.y - self.target.position.y) ** 2)
                if distance > self.view_range + 0.5:
                    self.target = None

                # Проверка находится ли цель в зоне атаки
                if distance < self.attack_range + 0.5:
                    # Тут дописать атаку
                    return

                # Движение монстра к цели
                self.updates_num_from_last_move += 1
                if not self.updates_num_from_last_move >= self.updates_to_move:
                    return
                else:
                    self.updates_num_from_last_move = 0

                move_delta = Vector2()
                if self.position.x < self.target.position.x:
                    move_delta.x = 1
                if self.position.x > self.target.position.x:
                    move_delta.x = -1
                if self.position.y < self.target.position.y:
                    move_delta.y = 1
                if self.position.y > self.target.position.y:
                    move_delta.y = -1
                map_.add_new_delayed_action(Action(self, ActionType.move, move_delta))

        except Exception as exception:
            print(f'Непредвиденная ошибка в monster.process_monster_logics: {exception}')



