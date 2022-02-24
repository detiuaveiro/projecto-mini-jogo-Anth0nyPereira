from enum import Enum


class PlayerState(Enum):
    WITHOUT_FOOD = 0
    WITH_FOOD = 1


class EntityState(Enum):
    SLEEPING = 0
    AWAKE = 1
