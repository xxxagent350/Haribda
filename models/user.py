
# Класс пользователя, хранящий его достижения, настройки, и т. д.
class User:
    def __init__(self, user_id, name = "No name", artefacts=None):
        if artefacts is None:
            artefacts = []
        self.id = user_id
        self.name = name
        self.artefacts = artefacts
        self.special_info = ""
