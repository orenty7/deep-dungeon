import pygame

from enums import PlayerState, Direction
from tile_loader import characters

S = 1.5


class Player:
    speed = 500
    def __init__(self, pos):
        self.pos = [*pos]
        self.size = [128, 128]

        self.frames = {
            PlayerState.Stand: [characters[1][0]],
            PlayerState.Walk: characters[1][:4:],
            PlayerState.Jump: [characters[1][5]]
        }
        self.frame = 0
        self.rect = pygame.Rect((self.pos, self.size))
        self.state = PlayerState.Stand
        self.direction = Direction.Right

    def move(self, vec):
        dx, dy = vec
        new_pos = [*self.pos]
        new_pos[0] += dx
        new_pos[1] += dy

        self.pos = new_pos

    def sit(self):
        return
        if not self.state['sitting']:
            self.state['sitting'] = True
            self.pos[1] += self.size[1] * (1 - 1 / S)
            self.size[1] /= S

    def unsit(self):
        return
        if self.state['sitting']:
            self.state['sitting'] = False
            self.pos[1] -= self.size[1] * (S - 1)
            self.size[1] *= S

    def set_state(self, new_state):
        if self.state != new_state:
            print(new_state)
            self.frame = 0
            self.state = new_state

    def set_moving_direction(self, direction):
        self.direction = direction

    def next_frame(self):
        self.frame += 1
        self.frame %= len(self.frames[self.state])

    def draw(self, screen, pos):
        blitting_pos = (
            pos[0],
            pos[1] + 128 - self.frames[self.state][self.frame].get_height()
        )
        image = self.frames[self.state][self.frame]
        if self.direction == Direction.Left:
            image = pygame.transform.flip(image, True, False)
        screen.blit(image, pos)

    def rectangle(self):
        return pygame.Rect(self.pos, self.size)
