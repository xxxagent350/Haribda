# Класс корабля, хранящий его статы
from models.world_objects.game_object import GameObject
from models.world_objects.Сharacter import Сharacter


class Ship(GameObject):
    def __init__(self, owner, position, sprite_name, rotation, max_hp, field_of_view = 5):
        """

        :param owner: Владелец
        :param position: Стартовая позиция
        :param sprite_name: Название текстуры
        :param rotation: Поворот
        :param max_hp: Максимальные ХП
        :param field_of_view: Хрен знает
        """
        super().__init__(position)
        self.owner = owner

        self.sprite_name = sprite_name
        self.rotation = rotation
        self.max_hp = max_hp
        self.hp = max_hp
        self.field_of_view = field_of_view

        self.onboard_team = []

        self.onboard_team.append(Сharacter(True,1))
        self.onboard_team.append(Сharacter())
        self.onboard_team.append(Сharacter())

    def take_damage(self,damage):
        """
        Функция получения кораблём урона и проверки на уничтожение.
        :param damage: Целое положительное число
        :return: Удалось ли этой атаке уничтожить корабль
        """
        self.hp = self.hp - damage
        if self.hp < 0:
            return True
        else:
            return False
        #При hp = 0 корабль должен получать урон за каждое перемещение с шансом зависящим от опыта управления капитана


