from core.vector2 import Vector2


class Island:
    def __init__(self, local_points=None):
        if local_points is None:
            local_points = [Vector2(0, 0)]
        self.local_points = local_points
