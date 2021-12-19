import pygame

from enums import Key, KeyState, PlayerState, Direction
from tiles import Tile
from .renderer import Renderer

class Engine:
    def __init__(self, tiles, player, world_settings, window):
        self.tiles = tiles
        self.player = player
        self.gravity = world_settings['gravity']

        self.key_state = {
            Key.W: KeyState.UnPressed,
            Key.A: KeyState.UnPressed,
            Key.S: KeyState.UnPressed,
            Key.D: KeyState.UnPressed,
            Key.Space: KeyState.UnPressed
        }
        self.renderer = Renderer(tiles, player, window)
        self.i = 0
        self.screen_pos = self.player.pos


    def draw(self, screen):
        self.renderer.render(screen)

    def keydown(self, key):
        self.key_state[key] = KeyState.Pressed

    def keyup(self, key):
        self.key_state[key] = KeyState.UnPressed

    def can_move(self, motion):
        rect = self.player.rectangle()
        rect = rect.move(motion)
        tile_rects = list(map(Tile.rectangle, self.tiles))
        return rect.collidelist(tile_rects) == -1



    def tick(self, dt):
        self.renderer.tick(dt)

        if self.i % 10 == 0:
            self.player.next_frame()
        self.i += 1

        if self.key_state[Key.Space] == KeyState.Pressed and self.player.on_ground:
            self.player.velocity[1] = -400
            self.player.set_state(PlayerState.Jump)


        if self.key_state[Key.D] == KeyState.Pressed:
            self.player.velocity[0] = self.player.speed
            self.player.set_moving_direction(Direction.Right)
        elif self.key_state[Key.A] == KeyState.Pressed:
            self.player.velocity[0] = -self.player.speed
            self.player.set_moving_direction(Direction.Left)
        else:
            self.player.velocity[0] = 0

        motion = (
            self.player.velocity[0] * dt,
            self.player.velocity[1] * dt
        )

        if self.can_move((motion[0], 0)):
            self.player.pos[0] += motion[0]

        if self.player.state != PlayerState.Jump:
            if motion[0] != 0:
                self.player.set_state(PlayerState.Walk)
            else:
                self.player.set_state(PlayerState.Stand)

        if self.can_move((0, motion[1])):
            self.player.pos[1] += motion[1]
        else:
            if motion[1] > 0:
                if self.player.state == PlayerState.Jump:
                    self.player.set_state(PlayerState.Stand)
            self.player.pos[1] -= 0.01
            self.player.velocity[1] = 0


        if not self.player.on_ground:
            self.player.velocity[1] += self.gravity * dt


    # player_state = {
    #     'moving direction': 'UP',
    #     'on ground': True
    # }
