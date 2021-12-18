import pygame

from enums import PlayerState, Direction
from tile_loader import characters

S = 1.5

def hitbox(sprite):
    bound_min_x = 0
    bound_min_y = 0
    bound_max_x = sprite.get_width()
    bound_max_y = sprite.get_height()

    found = False
    for y in range(sprite.get_height()):
        for x in range(sprite.get_width()):
            if sprite.get_at((x, y)) != (255, 255, 255, 0):
                bound_min_y = y
                found = True
        if found:
            break
    found = False
    for y in reversed(range(sprite.get_height())):
        for x in range(sprite.get_width()):
            if sprite.get_at((x, y)) != (255, 255, 255, 0):
                bound_max_y = y + 1
                found = True
        if found:
            break

    found = False
    for x in range(sprite.get_width()):
        for y in range(sprite.get_height()):
            if sprite.get_at((x, y)) != (255, 255, 255, 0):
                bound_min_x = x
                found = True
        if found:
            break

    found = False
    for x in reversed(range(sprite.get_width())):
        for y in range(sprite.get_height()):
            if sprite.get_at((x, y)) != (255, 255, 255, 0):
                bound_max_x = x + 1
                found = True
        if found:
            break

    return (bound_min_x, bound_min_y), (bound_max_x - bound_min_x, bound_max_y - bound_min_y)


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
