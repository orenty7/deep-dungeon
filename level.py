from engine import Engine
from player import Player
from settings import FPS


# setting the class level
class Level:
    def __init__(self, player_pos, tiles, settings):
        self.engine = None
        self.player = Player(player_pos)
        self.tiles = tiles

        settings = {
            'gravity': 1200
        }
        self.settings = settings

    def init_engine(self, window):
        self.engine = Engine(self.tiles, self.player, self.settings, window)

    def tick(self, screen, events):
        screen.fill('white')
        self.engine.tick(1 / FPS)
        self.engine.draw(screen)
