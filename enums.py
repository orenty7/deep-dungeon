from enum import Enum


class Direction(Enum):
    Up = 0
    Left = 1
    Down = 2
    Right = 3


class Key(Enum):
    W = 0
    D = 1
    S = 2
    A = 3


class KeyState(Enum):
    Pressed = 0
    UnPressed = 1
