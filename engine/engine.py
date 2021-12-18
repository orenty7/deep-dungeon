import pygame

from enums import Key, KeyState, PlayerState, Direction


class Engine:
    def __init__(self, tiles, player, world_settings):
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

        self.moving = {
            'velocity': [0, 0],
            'on ground': False
        }
        self.i = 0
        self.render()

    def render(self):
        surface = pygame.Surface((64 * 100, 64 * 24))
        surface.fill((102, 224, 189))
        visible_part = pygame.Rect((self.player.pos[0] - 100, 0), (64 * 20, 64 * 12))
        for tile in self.tiles:
            tile.draw(surface)
        self.surface = surface

    def draw(self, screen):
        blitting_pos = (-self.player.pos[0] + 200, 0)
        screen.blit(self.surface, blitting_pos)
        self.player.draw(screen, (200, self.player.pos[1]))

    def keydown(self, key):
        self.key_state[key] = KeyState.Pressed

    def keyup(self, key):
        self.key_state[key] = KeyState.UnPressed

    def tick(self, dt):
        motion = self.moving['velocity']

        if self.i % 10 == 0:
            self.player.next_frame()
        self.i += 1

        if self.key_state[Key.Space] == KeyState.Pressed and self.moving['on ground']:
            motion[1] = -4
            self.player.set_state(PlayerState.Jump)


        if self.key_state[Key.D] == KeyState.Pressed:
            motion[0] = self.player.speed * dt
            self.player.set_moving_direction(Direction.Right)
        elif self.key_state[Key.A] == KeyState.Pressed:
            motion[0] = -self.player.speed * dt
            self.player.set_moving_direction(Direction.Left)
        else:
            motion[0] = 0

        if self.player.state != PlayerState.Jump:
            if motion[0] != 0:
                self.player.set_state(PlayerState.Walk)
            else:
                self.player.set_state(PlayerState.Stand)

        self.player.move((motion[0], 0))
        for tile in self.tiles:
            if tile.rectangle().colliderect(self.player.rectangle()):
                self.player.move((-motion[0], 0))
                break

        self.player.move((0, motion[1]))
        for tile in self.tiles:
            if tile.rectangle().colliderect(self.player.rectangle()):
                if motion[1] > 0:
                    self.moving['on ground'] = True
                    if self.player.state == PlayerState.Jump:
                        self.player.set_state(PlayerState.Stand)

                self.player.move((0, -motion[1]))
                self.player.move((0, -0.5))
                motion[1] = 0
                break
        else:
            self.moving['on ground'] = False

        if not self.moving['on ground']:
            motion[1] += self.gravity * dt
        self.moving['velocity'] = motion

    # player_state = {
    #     'moving direction': 'UP',
    #     'on ground': True
    # }
