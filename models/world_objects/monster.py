from models.world_objects.game_object import GameObject
from core import images_operator


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
