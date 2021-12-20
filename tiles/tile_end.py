from .tile import Tile


class TileEnd(Tile):
    def __init__(self, pos, cors_in_spritesheet=None):
        super().__init__(pos, cors_in_spritesheet)
        self.type = 'end'
