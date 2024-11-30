from DB_operators.BD_init import add_user, get_user, save_user
from models.world_objects.ship import Ship
from core.vector2 import Vector2
from core.map_list import maps



# Класс пользователя, хранящий его достижения, настройки, и т. д.
class User:
    def __init__(self, user_id):
        global user_list
        #Тут часто используемые
        self.id = user_id
        self.name = ' ___ '
        self.artefacts = []
        self.special_info = []
        self.controlled_ship = None
        self.current_map = 0
        self.map_message_id = None

        #получение информации об игроке с таким ID из базы данных
        user, examination = get_user(user_id)

        if examination:
            self.name, self.artefacts, self.special_info, self.current_map  = user[1:]
        else:
            self.__new_user()
            self.controlled_ship = Ship(self,Vector2(0,0),0, "ship1",100, 4)
            maps[0].add_new_object(self.controlled_ship)
            maps[0].add_new_object(Ship(self, Vector2(2, 2), 0, "ship3", 100, 4))



    def __new_user(self, name = "No name", artefacts=None, special_info = None):
        add_user(self.id,name)

    def save_user(self):
        save_user(self.id, self.name , self.artefacts, self.special_info, self.current_map)
