import pygame

from enum import Enum

class Key(Enum):
    W = 0
    D = 1
    S = 2
    A = 3
    Space = 4


class KeyState(Enum):
    Pressed = 0
    UnPressed = 1

class KeyManager:
    def __getitem__(self, item):
        return KeyState.Pressed if self.is_pressed(item) else KeyState.UnPressed

    def is_pressed(self, item):
        if item == Key.W:
            return pygame.key.get_pressed()[pygame.K_w]
        elif item == Key.A:
            return pygame.key.get_pressed()[pygame.K_a]
        elif item == Key.S:
            return pygame.key.get_pressed()[pygame.K_s]
        elif item == Key.D:
            return pygame.key.get_pressed()[pygame.K_d]
        elif item == Key.Space:
            return pygame.key.get_pressed()[pygame.K_SPACE]

