from models.world_objects.game_object import GameObject


class Monster(GameObject):
    def __init__(self, position, rotation, sprite_name, max_hp, view_range = 3, freeze_rotation=False, updates_to_move = 1):
        super().__init__(position, rotation)
