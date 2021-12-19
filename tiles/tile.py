import pygame

from tile_loader import sprites
from utils import hitbox

class Tile:
    def __init__(self, pos, cors_in_spritesheet):
        self.image = sprites[cors_in_spritesheet[1]][cors_in_spritesheet[0]]
        size = hitbox(self.image)
        self.rect = pygame.Rect((pos, size[1]))

    def rectangle(self):
        return self.rect

    def draw(self, screen):
        pygame.draw.rect(screen, 'black', self.rect, 2)
        screen.blit(self.image, self.rect.topleft)