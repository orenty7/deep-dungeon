from engine import Engine
from player import Player


class Level:
    def __init__(self, player_pos, tiles, settings, window):
        player = Player(player_pos)
        engine = Engine(player_pos, tiles, settings, window)
