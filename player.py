import pygame

S = 1.5

class Player:
    def __init__(self, rect):
        rect = pygame.Rect(rect)
        self.pos = [*rect.topleft]
        self.size = [*rect.size]
        self.state = {
            'sitting': False,
        }

    def move(self, vec):
        dx, dy = vec
        new_pos = [*self.pos]
        new_pos[0] += dx
        new_pos[1] += dy

        self.pos = new_pos
    def sit(self):
        if not self.state['sitting']:
            self.state['sitting'] = True
            self.pos[1] += self.size[1] * (1 - 1/S)
            self.size[1] /= S

    def unsit(self):
        if self.state['sitting']:
            self.state['sitting'] = False
            self.pos[1] -= self.size[1] * (S - 1)
            self.size[1] *= S


    def draw(self, screen):
        pygame.draw.rect(screen, 'blue', (self.pos, self.size), 2)

    def rectangle(self):
        return pygame.Rect(self.pos, self.size)
