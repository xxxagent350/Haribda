from DB_operators.BD_init import add_user

# Класс пользователя, хранящий его достижения, настройки, и т. д.
class User:
    def __init__(self, user_id):
        self.id = user_id
        self.name = ' ___ '
        self.artefacts = []
        self.special_info = ""
        self.new_user()


    def new_user(self, name = "No name", artefacts=None):
        add_user(self.id,name)
