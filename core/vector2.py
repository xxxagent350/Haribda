
class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, delta_pos):
        self.x += delta_pos.x
        self.y += delta_pos.y

    def to_str(self):
        return f'Vector2({self.x}, {self.y})'
