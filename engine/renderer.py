import pygame


class Renderer:
    screen_acceleration = 5
    background = (102, 224, 189)
    def __init__(self, tiles, player, window):

        min_x, min_y = tiles[0].rectangle().bottomleft
        max_x, max_y = tiles[0].rectangle().topright
        for tile in tiles:
            rect = tile.rectangle()
            min_x = min(min_x, rect.bottomleft[0])
            min_y = min(min_y, rect.bottomleft[1])

            max_x = max(max_x, rect.topright[0])
            max_y = max(max_y, rect.topright[1])

        self.rect = pygame.Rect((min_x, min_y), (max(window[0], max_x - min_x), max(window[1], max_y - min_y)))
        self.surface = pygame.Surface(self.rect.size)
        self.tiles = tiles
        self.player = player
        self.screen_pos = player.pos
        self.window = window

        self.render_tiles()

    def render_tiles(self):
        self.surface.fill(Renderer.background)
        for tile in self.tiles:
            tile.draw(self.surface)


    def tick(self, dt):
        self.screen_pos = [
            self.screen_pos[0] + ((self.player.pos[0] - self.window[0] / 2) - self.screen_pos[0]) * dt * Renderer.screen_acceleration,
            0
        ]
        self.screen_pos[0] = max(self.screen_pos[0], 256)


    def render(self, screen):
        player_blitting_pos = (
            self.player.pos[0] - self.screen_pos[0],
            self.player.pos[1] - self.screen_pos[1]
        )

        screen.blit(self.surface, (-self.screen_pos[0], -self.screen_pos[1]))
        self.player.draw(screen, player_blitting_pos)