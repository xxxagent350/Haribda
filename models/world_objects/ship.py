# Класс корабля, хранящий его статы
from models.world_objects.game_object import GameObject


class Ship(GameObject):
    def __init__(self, owner, position, sprite_name, rotation, max_hp, field_of_view = 5):
        super().__init__(position)
        self.owner = owner

        self.sprite_name = sprite_name
        self.rotation = rotation
        self.max_hp = max_hp
        self.hp = max_hp
        self.field_of_view = field_of_view
