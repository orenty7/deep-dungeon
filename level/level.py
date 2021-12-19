from player import Player
from engine import Engine


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

