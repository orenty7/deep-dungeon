import pygame

from player import Player
from engine import Engine
from settings import FPS


class Level:
    def __init__(self, player_pos, tiles, settings=None):
        self.engine = None
        self.player = Player(player_pos)
        self.tiles = tiles

        if settings is None:
            settings = {}
            settings['gravity'] = 1200
        self.settings = settings

    def init_engine(self, window):
        self.engine = Engine(self.tiles, self.player, self.settings, window)


    def tick(self, screen, events):
        screen.fill('white')
        self.engine.tick(1 / FPS)
        self.engine.draw(screen)

    def is_won(self):
        return self.engine.is_won()
