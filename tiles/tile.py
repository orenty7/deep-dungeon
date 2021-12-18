import pygame

from tile_loader import sprites

class Tile:
    def __init__(self, rect, cors):
        self.rect = pygame.Rect(rect)
        self.image = sprites[cors[0]][cors[1]]

    def rectangle(self):
        return self.rect

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)