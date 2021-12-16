import typing

from .tile import Tile, point
import pygame


class Platform(Tile):
    def __init__(self, rect):
        self.rect = pygame.Rect(rect)

    def rectangle(self):
        return self.rect

    def draw(self, screen):
        pygame.draw.rect(screen, 'red', self.rect, 2)

    @staticmethod
    def create(args) -> Tile:
        ...
