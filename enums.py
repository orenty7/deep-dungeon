from enum import Enum


class Direction(Enum):
    Left = 0
    Right = 1


class PlayerState(Enum):
    Sit = 0
    Jump = 1
    Walk = 2
    Stand = 3


class WindowState(Enum):
    Game = 0
    Pause = 1
    MainMenu = 2
    GameOver = 3
