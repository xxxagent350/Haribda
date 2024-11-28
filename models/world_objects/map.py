
class Map:
    def __init__(self):
        self.objects = []
        self.delayed_actions = [] # Действия, находящиеся в списке ожидания
        self.changed_squares = [] # Квадраты, на которых в были зафиксированы изменения(если такой квадрат находиться в поле видимости у игрока, то стоит перевыслать ему изображение карты)

    def add_changed_square(self, object_):
        self.changed_squares.append(object_.position)
        print(f"added {object_}: {self.delayed_actions}")
