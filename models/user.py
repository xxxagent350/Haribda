from DB_operators.BD_init import add_user, get_user, save_user


# Класс пользователя, хранящий его достижения, настройки, и т. д.
class User:
    def __init__(self, user_id):
        #Тут часто используемые
        self.id = user_id
        self.name = ' ___ '
        self.artefacts = []
        self.special_info = []
        self.controlled_ship = None
        self.current_map = None
        self.map_message_id = None

        #получение информации об игроке с таким ID из базы данных
        user, examination = get_user(user_id)

        if examination:
            self.name, self.artefacts, self.special_info = user[1:]
        else:
            self.__new_user()
        print(self.name, self.artefacts, self.special_info)


    def __new_user(self, name = "No name", artefacts=None, special_info = None):
        add_user(self.id,name)

    def save_user(self):
        save_user(self.id, self.name , self.artefacts, self.special_info)
