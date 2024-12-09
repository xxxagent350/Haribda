from core.images_operator import get_image_path_from_ship_name
from core.vector2 import Vector2
from models.user import User
from models.world_objects.game_object import GameObject
from models.world_objects.Character import Character


# Класс корабля, хранящий его статы
class Ship(GameObject):
    def __init__(self, position, rotation, sprite_name, max_hp = 100, view_range = 4):
        """
        :param position: Стартовая позиция
        :param rotation: Стартовый поворот
        :param sprite_name: Название текстуры
        :param max_hp: Максимальные ХП
        :param view_range: Радиус обзора в клетках (целое)
        """
        super().__init__(position, rotation, get_image_path_from_ship_name(sprite_name))
        self.owner = None
        self.max_hp = max_hp
        self.hp = max_hp
        self.view_range = view_range

        self.onboard_team = []

        self.onboard_team.append(Character(True, 1))
        self.onboard_team.append(Character())
        self.onboard_team.append(Character())

    def register_owner(self, owner):
        """Регистрирует владельца корабля"""
        self.owner = owner
        if type(owner) == User:
            owner.controlled_ship = self


    def move(self, direction):
        self.rotation = direction
        match direction:
            case 0:  # Вверх
                self.position.add(Vector2(0, 1))
            case 45:
                self.position.add(Vector2(-1, 1))
            case -45:
                self.position.add(Vector2(1, 1))
            case 90:
                self.position.add(Vector2(-1, 0))
            case -90:
                self.position.add(Vector2(1, 0))
            case 135:
                self.position.add(Vector2(-1, -1))
            case -135:
                self.position.add(Vector2(1, -1))
            case 180:
                self.position.add(Vector2(0, -1))


    def take_damage(self,damage):
        """
        Функция получения кораблём урона и проверки на уничтожение.
        :param damage: Целое положительное число
        :return: удалось ли этой атаке уничтожить корабль
        """
        self.hp -= damage
        if self.hp < 0:
            return True
        else:
            return False
        # При hp <= 0 корабль должен получать урон за каждое перемещение с шансом, зависящим от опыта управления капитана


