import time

from numpy.random import randint


class GameObject:
    def __init__(self, position, rotation = 0, image_path = None, scale = 1):
        self.index = f'{time.time()}_{randint(0, 1000000000)}_{randint(0, 1000000000)}'
        self.position = position
        self.rotation = rotation
        self.image_path = image_path
        self.scale = scale
