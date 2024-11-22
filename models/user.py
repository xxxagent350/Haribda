from DB_operators.BD_init import add_user, get_user


# Класс пользователя, хранящий его достижения, настройки, и т. д.
class User:
    def __init__(self, user_id):
        self.id = user_id
        self.name = ' ___ '
        self.artefacts = []
        self.special_info = ""

        user, examination = get_user(user_id)

        if examination:
            self.name, self.artefacts, self.special_info = user[1:]
        else:
            self.new_user()
        print(self.name, self.artefacts, self.special_info)


    def new_user(self, name = "No name", artefacts=None):
        add_user(self.id,name)
