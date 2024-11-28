
class Map:
    def __init__(self):
        self.objects = []
        self.delayed_actions = [] # Действия, находящиеся в списке ожидания (передвижение корабля/существа, ныряние, постройка и т. д.)
        self.short_delayed_actions = []  # Короткие действия, находящиеся в списке ожидания (полёт снаряда, взрыв и т. д.)
        self.changed_squares = [] # Квадраты, на которых в были зафиксированы изменения(если такой квадрат находиться в поле видимости у игрока, то стоит перевыслать ему изображение карты)

    def add_new_object(self, object_):
        self.objects.append(object_)
        self.add_changed_square(object_)

    def add_new_delayed_action(self, delayed_action, short_action = False):
        if not short_action:
            self.delayed_actions.append(delayed_action)
        else:
            self.short_delayed_actions.append(delayed_action)

    # Проверяет есть ли у объекта ожидаемые действия. Полезно для проверки есть ли уже у корабля действия в списке ожиданий, чтобы он не мог совершить более 1 действия за ход
    def check_if_object_has_delayed_actions(self, object_, short_actions = False):
        if not short_actions:
            delayed_actions_list = self.delayed_actions
        else:
            delayed_actions_list = self.short_delayed_actions

        for delayed_action in delayed_actions_list:
            if delayed_action.object_ == object_:
                return True
        return False

    def add_changed_square(self, object_):
        self.changed_squares.append(object_.position)
