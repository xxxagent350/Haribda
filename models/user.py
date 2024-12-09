from DB_operators.BD_init import add_user, get_user, save_user

from DB_operators.BD_init import get_all_user_ids


# Класс пользователя, хранящий его достижения, настройки, и т. д.
class User:
    def __init__(self, user_id):
        global users_dict
        #Тут часто используемые
        self.id = user_id
        self.name = ' ___ '
        self.artefacts = []
        self.special_info = []
        self.current_map = 0
        self.map_message_id = None

        self.controlled_ship = None;  """Задавать с помощью ship.register_owner(owner)"""


        #получение информации об игроке с таким ID из базы данных
        user, examination = get_user(user_id)

        
        if examination:
            self.name, self.artefacts, self.special_info, self.controlled_ship, self.current_map  = user[1:]

            if self.current_map is None:
                self.current_map = 0
        else:
            self.__new_user()
            #self.controlled_ship = Ship(self,Vector2(0,0),0, "ship 1",100, 4)
            #maps[0].add_new_object(self.controlled_ship)
            #print(maps[0].objects)
            #maps[0].add_new_object(Ship(self, Vector2(2, 2), 0, "ship 3", 100, 4))
        users_dict[user_id] = self




    def __new_user(self, name = "No name", artefacts=None, special_info = None):
        add_user(self.id,name)

    def save_user(self):
        save_user(self.id, self.name , self.artefacts, self.special_info, self.current_map, self.controlled_ship != None)


users_id  = get_all_user_ids()
users_dict = {}

for i in users_id:
    User(i)