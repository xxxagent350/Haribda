from core.vector2 import Vector2
from models.world_objects.game_object import GameObject


class Island(GameObject):
    def __init__(self, position, local_points=None):
        if local_points is None:
            local_points = [Vector2(0, 0)]
        super().__init__(position)
        self.local_points = local_points
