from enum import Enum


class ActionType(Enum):
    move = 0,
    attack = 1,
    dive = 2


class Action():
    def __init__(self, action_type, value):
        self.action_type = action_type
        self.value = value
