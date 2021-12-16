from enums import Direction, Key, KeyState

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
        }

        self.moving = {
            'velocity': [0, 0]
        }


    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)

        self.player.draw(screen)

    def keydown(self, key):
        self.key_state[key] = KeyState.Pressed

    def keyup(self, key):
        self.key_state[key] = KeyState.UnPressed

    def tick(self, dt):
        velocity = self.moving['velocity']
        if self.player.state['sitting'] and self.key_state[Key.S] == KeyState.UnPressed:
            self.player.unsit()


        if self.key_state[Key.D] == KeyState.Pressed:
            velocity[0] = 10
        elif self.key_state[Key.A] == KeyState.Pressed:
            velocity[0] = -10
        else:
            velocity[0] = 0

        self.player.move((velocity[0], 0))
        for tile in self.tiles:
            if tile.rectangle().colliderect(self.player.rectangle()):
                self.player.move((-velocity[0], 0))
                break

        self.player.move((0, velocity[1]))
        for tile in self.tiles:
            if tile.rectangle().colliderect(self.player.rectangle()):
                if velocity[1] > 0:
                    self.player.sit()
                self.player.move((0, -velocity[1]))
                velocity[1] = 0
                break

        velocity[1] += self.gravity * dt
        self.moving['velocity'] = velocity






    # player_state = {
    #     'moving direction': 'UP',
    #     'on ground': True
    # }
