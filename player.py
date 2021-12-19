import pygame

from enums import PlayerState, Direction
from utils import hitbox
from tile_loader import characters


class Player:
    speed = 500
    def __init__(self, pos):
        self.pos = [*pos]

        self.frames = {
            PlayerState.Stand: [characters[1][0]],
            PlayerState.Walk: characters[1][:4:],
            PlayerState.Jump: [characters[1][5]]
        }
        self.frame = 0
        self.state = PlayerState.Stand
        self.direction = Direction.Right

        self.hitbox = pygame.Rect(hitbox(self.frames[self.state][self.frame]))
        self.size = self.hitbox.size



    def move(self, vec):
        dx, dy = vec
        new_pos = [*self.pos]
        new_pos[0] += dx
        new_pos[1] += dy

        self.pos = new_pos


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
        image = self.frames[self.state][self.frame]
        if self.direction == Direction.Left:
            image = pygame.transform.flip(image, True, False)

        screen.blit(image, pos)

    def rectangle(self):
        return pygame.Rect((
            self.pos[0] + self.hitbox.topleft[0],
            self.pos[1] + self.hitbox.topleft[1]),
            self.size
        )
