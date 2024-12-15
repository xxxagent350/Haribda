
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
        self.controlled_ship_id = None # Уникальный идентификатор корабля(нужен при загрузке данных из файла)


        '''
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
        '''
