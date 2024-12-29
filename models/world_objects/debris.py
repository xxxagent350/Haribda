from core.images_operator import get_image_path_from_effect_name
from models.action import Action, ActionType
from models.world_objects.game_object import GameObject


class Debris(GameObject):
    def __init__(self, position, rotation, sprite_name, lifetime=60):
        """
        :param position: Позиция обломков
        :param rotation: Поворот обломков
        :param sprite_name: Название текстуры обломков
        :param lifetime: Время существования обломков в обновлениях
        """
        super().__init__(position, rotation, get_image_path_from_effect_name(sprite_name))
        self.lifetime = lifetime  # Количество обновлений до удаления

    def decrement_lifetime(self, map_, delta = 1):
        """Уменьшает оставшееся время жизни обломков. Если время истекло, возвращает True."""
        self.lifetime -= delta
        if self.lifetime <= 0:
            map_.add_new_delayed_action(Action(self, ActionType.destroy), True, False)
