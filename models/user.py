from models.world_objects.ship import Ship
from variables.maps_dict import maps


# Класс пользователя, хранящий его достижения, настройки, и т. д.
class User:
    def __init__(self, user_id, name='not_set', artefacts=None, special_info ='', current_map_num = 0, controlled_ship_id = None):
        """
        :param user_id: ID пользователя
        :param name: Имя
        :param artefacts: Артефакты
        :param special_info: Дополнительная информация
        :param current_map_num: Номер текущей карты, на которой находится корабль игрока
        :param controlled_ship_id: ID корабля, которым владеет пользователь. Будет выполнен поиск корабля по всем картам и зарегистрирован владелец корабля
        """
        #Тут часто используемые
        if artefacts is None:
            artefacts = []
        self.id = user_id
        self.name = name
        self.artefacts = artefacts
        self.special_info = special_info
        self.current_map_num = current_map_num
        self.map_message_id = None
        self.controlled_ship = None

        if controlled_ship_id is not None:
            # Поиск корабля по ID
            searching_complete = False
            for map_ in maps.values():
                for object_ in map_.objects:
                    if type(object_) == Ship and object_.index == controlled_ship_id:
                        object_.register_owner(self)
                        searching_complete = True
                        break
                if searching_complete:
                    break


