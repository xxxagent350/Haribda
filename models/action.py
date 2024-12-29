from enum import Enum


class ActionType(Enum):
    move = 0,
    attack = 1,
    dive = 2,
    destroy = 3


class Action:
    def __init__(self, object_, action_type, value = None):
        self.object_ = object_
        self.action_type = action_type
        self.value = value
