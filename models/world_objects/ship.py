# Класс корабля, хранящий его статы
from models.world_objects.game_object import GameObject


class Ship(GameObject):
    def __init__(self, position, sprite_name, rotation, max_hp):
        super().__init__(position)
        self.sprite_name = sprite_name
        self.rotation = rotation
        self.max_hp = max_hp
        self.hp = max_hp
