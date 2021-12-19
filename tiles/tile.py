import pygame

from tile_loader import sprites
from utils import hitbox

class Tile:
    def __init__(self, pos, cors_in_spritesheet):
        self.image = sprites[cors_in_spritesheet[1]][cors_in_spritesheet[0]]
        size = hitbox(self.image)
        self.pos = pos
        self.rect = pygame.Rect((pos[0] + size[0][0], pos[1] + size[0][1]), size[1])

    def rectangle(self):
        return self.rect

    def draw(self, screen):
        pygame.draw.rect(screen, 'black', self.rect, 2)
        screen.blit(self.image, self.pos)