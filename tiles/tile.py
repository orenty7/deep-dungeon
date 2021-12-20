import pygame

from tile_loader import sprites
from utils import hitbox


class Tile:
    def __init__(self, pos, cors_in_spritesheet=None):
        self.pos = pos
        self.image = None
        self.type = 'common'
        if cors_in_spritesheet is not None:
            self.image = sprites[cors_in_spritesheet[1]][cors_in_spritesheet[0]]
            size = hitbox(self.image)
            self.rect = pygame.Rect((pos[0] + size[0][0], pos[1] + size[0][1]), size[1])
        else:
            size = (64, 64)
            self.rect = pygame.Rect((pos[0], pos[1]), size)

    def rectangle(self):
        return self.rect

    def draw(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.pos)
