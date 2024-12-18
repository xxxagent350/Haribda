from models.world_objects.game_object import GameObject
from core import images_operator


class Monster(GameObject):
    def __init__(self, position, rotation, sprite_name, max_hp, scale = 1, agr_range = 3, freeze_rotation_at = None, updates_to_move = 1):
        """
        Монстр
        :param position: стартовая позиция
        :param rotation: стартовый поворот
        :param sprite_name: название спрайта
        :param max_hp: максимальное здоровье
        :param agr_range: радиус агра
        :param freeze_rotation_at: укажите поворот изображения в градусах (None = автоматический поворот в сторону движения)
        :param updates_to_move: раз в сколько обновлений будет двигаться монстр (1 = со скоростью игрока, 2 = в 2 раза медленнее)
        """
        super().__init__(position, rotation, images_operator.get_image_path_from_monster_name(sprite_name), scale)
        self.max_hp = max_hp
        self.agr_range = agr_range
        self.freeze_rotation_at = freeze_rotation_at
        self.updates_to_move = updates_to_move
