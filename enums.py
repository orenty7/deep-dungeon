from enum import Enum


class Direction(Enum):
    Left = 0
    Right = 1


class PlayerState(Enum):
    Sit = 0
    Jump = 1
    Walk = 2
    Stand = 3


class Key(Enum):
    W = 0
    D = 1
    S = 2
    A = 3
    Space = 4


class KeyState(Enum):
    Pressed = 0
    UnPressed = 1
