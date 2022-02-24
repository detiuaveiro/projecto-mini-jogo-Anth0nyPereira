from enum import Enum


class PlayerState(Enum):
    """
    Enum that stores the 2 available states for the player
    """
    WITHOUT_FOOD = 0
    WITH_FOOD = 1


class EntityState(Enum):
    """
    Enum that stores the 2 available states for the entity
    """
    SLEEPING = 0
    AWAKE = 1
