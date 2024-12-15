
class DBColumn:
    def __init__(self, name : str, type_ : str, default = None, not_null = False):
        """
        :param name: Название ячейки в базе данных
        :param type_: Тип ячейки в базе данных, например INTEGER или TEXT
        :param default: Значение по умолчанию
        :param not_null: Может ли быть null
        """
        self.name = name
        self.type_ = type_
        self.default = default
        self.not_null = not_null
