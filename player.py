import pygame

from enums import PlayerState, Direction
from tile_loader import characters
from utils import hitbox


class Player:
    speed = 500

    def __init__(self, pos):
        self.pos = [*pos]
        self.velocity = [0, 0]
        self.frames = {
            PlayerState.Stand: [characters[1][0]],
            PlayerState.Walk: characters[1][:4:],
            PlayerState.Jump: characters[1][5:8:],
            PlayerState.Snake: characters[3][:4:]
        }
        self.on_ground = False
        self.frame = 0
        self.state = PlayerState.Jump
        self.direction = Direction.Right

        self.hitbox = pygame.Rect(hitbox(self.frames[self.state][self.frame]))
        self.size = self.hitbox.size

    def set_state(self, new_state):
        if self.state != new_state:
            self.frame = 0
            self.state = new_state

            self.on_ground = self.state != PlayerState.Jump

    def set_moving_direction(self, direction):
        self.direction = direction

    def next_frame(self):
        if self.state == PlayerState.Jump:
            if self.velocity[1] >= 0:
                self.frame = 1
            else:
                self.frame = 0
            return
        self.frame += 1
        self.frame %= len(self.frames[self.state])

    def draw(self, screen, pos):
        image = self.frames[self.state][self.frame]
        if self.direction == Direction.Left:
            image = pygame.transform.flip(image, True, False)
        screen.blit(image, pos)

    def real_pos(self):
        return (
            self.pos[0] + self.hitbox.topleft[0],
            self.pos[1] + self.hitbox.topleft[1]
        )

    def rectangle(self):
        return pygame.Rect(
            self.real_pos(),
            self.size
        ).copy()
