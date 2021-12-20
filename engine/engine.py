import pygame

from enums import PlayerState, Direction
from tiles import Tile
from .key_manager import KeyManager, KeyState, Key
from .renderer import Renderer


class Engine:
    def __init__(self, tiles, player, world_settings, window):
        self.common_tiles = list(filter(lambda tile: tile.type == 'common', tiles))
        self.kill_tiles = list(filter(lambda tile: tile.type == 'kill', tiles))
        self.end_tiles = list(filter(lambda tile: tile.type == 'end', tiles))

        self.player = player
        self.gravity = world_settings['gravity']

        self.key_state = KeyManager()
        self.renderer = Renderer(tiles, player, window)
        self.i = 0
        self.screen_pos = self.player.pos

    def draw(self, screen):
        self.renderer.render(screen)

    def can_move(self, motion):
        rect = self.player.rectangle()
        rect = pygame.Rect((rect.topleft[0] + motion[0], rect.topleft[1] + motion[1]), rect.size)
        # rect = rect.move(motion)
        tile_rects = list(map(Tile.rectangle, self.common_tiles))
        return rect.collidelist(tile_rects) == -1

    def is_won(self):
        rect = self.player.rectangle()
        end_tile_rects = list(map(Tile.rectangle, self.end_tiles))
        kill_tile_rects = list(map(Tile.rectangle, self.kill_tiles))

        if rect.collidelist(kill_tile_rects) != -1:
            return False

        if rect.collidelist(end_tile_rects) != -1:
            return True
        return None

    def tick(self, dt):
        self.renderer.tick(dt)

        if self.i % 10 == 0:
            self.player.next_frame()
        self.i += 1

        if self.key_state[Key.Space] == KeyState.Pressed and self.player.on_ground:
            self.player.velocity[1] = -400
            self.player.set_state(PlayerState.Jump)

        self.player.velocity[0] = 0
        if self.key_state[Key.D] == KeyState.Pressed:
            self.player.velocity[0] += self.player.speed
            self.player.set_moving_direction(Direction.Right)
        if self.key_state[Key.A] == KeyState.Pressed:
            self.player.velocity[0] -= self.player.speed
            self.player.set_moving_direction(Direction.Left)

        motion = (
            self.player.velocity[0] * dt,
            self.player.velocity[1] * dt
        )

        if self.can_move((motion[0], 0)):
            self.player.pos[0] += motion[0]
        else:
            if motion[0] > 0:
                self.player.pos[0] -= 0.01
            elif motion[0] < 0:
                self.player.pos[0] += 0.01

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
                self.player.pos[1] -= 0.4
                self.player.velocity[1] = 0

            elif motion[1] < 0:
                self.player.pos[1] += 0.4
                self.player.velocity[1] = 0

        if self.can_move((0, 5)):
            self.player.velocity[1] += self.gravity * dt
