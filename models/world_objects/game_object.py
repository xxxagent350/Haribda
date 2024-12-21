import time

from numpy.random import randint

from core.vector2 import Vector2


class GameObject:
    def __init__(self, position, rotation = 0, image_path = None, scale = 1):
        self.index = f'{time.time()}_{randint(0, 1000000000)}_{randint(0, 1000000000)}'
        self.position = position
        self.rotation = rotation
        self.image_path = image_path
        self.scale = scale


    def try_move_at_dir(self, direction, map_) -> bool:
        self.rotation = direction
        match direction:
            case 0:  # Вверх
                return self.try_move_with_delta(Vector2(0, 1), map_)
            case 45:
                return self.try_move_with_delta(Vector2(-1, 1), map_)
            case -45:
                return self.try_move_with_delta(Vector2(1, 1), map_)
            case 90:
                return self.try_move_with_delta(Vector2(-1, 0), map_)
            case -90:
                return self.try_move_with_delta(Vector2(1, 0), map_)
            case 135:
                return self.try_move_with_delta(Vector2(-1, -1), map_)
            case -135:
                return self.try_move_with_delta(Vector2(1, -1), map_)
            case 180:
                return self.try_move_with_delta(Vector2(0, -1), map_)


    def try_move_with_delta(self, delta_position, map_) -> bool:
        if map_.check_if_square_is_free(self.position.summ(delta_position)):
            self.position.add(delta_position)
            return True
        else:
            return False
