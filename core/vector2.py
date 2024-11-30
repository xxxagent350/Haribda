
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, delta_pos):
        """Прибавляет к этому вектору другой"""
        self.x += delta_pos.x
        self.y += delta_pos.y

    def summ(self, delta_pos):
        """Возвращает сумму векторов"""
        return Vector2(self.x + delta_pos.x, self.y + delta_pos.y)

    def to_str(self):
        return f'Vector2({self.x}, {self.y})'

    def equals(self, compare_to) -> bool:
        if self.x == compare_to.x and self.y == compare_to.y:
            return True
        else:
            return False
