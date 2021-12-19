import pygame

from player import Player
from engine import Engine
from enums import Key
from settings import FPS


class Level:
    def __init__(self, player_pos, tiles, settings):
        self.engine = None
        self.player = Player(player_pos)
        self.tiles = tiles

        settings = {
            'gravity': 15
        }
        self.settings = settings

    def init_engine(self, window):
        self.engine = Engine(self.tiles, self.player, self.settings, window)

    def play(self):
        pygame.init()
        screen = pygame.display.set_mode((64 * 20, 64 * 12))
        clock = pygame.time.Clock()

        finished = False
        while not finished:
            clock.tick(FPS)

            screen.fill('white')
            self.engine.tick(1 / FPS)
            self.engine.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.KEYDOWN:
                    print(event)
                    if event.key == pygame.K_w:
                        self.engine.keydown(Key.W)
                    elif event.key == pygame.K_a:
                        self.engine.keydown(Key.A)
                    elif event.key == pygame.K_s:
                        self.engine.keydown(Key.S)
                    elif event.key == pygame.K_d:
                        self.engine.keydown(Key.D)
                    elif event.key == pygame.K_SPACE:
                        self.engine.keydown(Key.Space)
                elif event.type == pygame.KEYUP:
                    print(event)
                    if event.key == pygame.K_w:
                        self.engine.keyup(Key.W)
                    elif event.key == pygame.K_a:
                        self.engine.keyup(Key.A)
                    elif event.key == pygame.K_s:
                        self.engine.keyup(Key.S)
                    elif event.key == pygame.K_d:
                        self.engine.keyup(Key.D)
                    elif event.key == pygame.K_SPACE:
                        self.engine.keyup(Key.Space)

            pygame.display.update()

