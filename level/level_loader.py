import os

from .level import Level
from tiles import spritesheet, Tile
from settings import tile_size

def parse_level(lines):
    lines = list(filter(lambda s: s != '', map(str.strip, lines)))
    width, height = map(int, lines[0].split())
    player_pos = map(int, lines[1].split())

    tiles_str = map(str.split, lines[2::])

    x, y = (0, 0)
    tiles = []
    for line in tiles_str:
        for tile in line:
            if tile in spritesheet:
                tiles.append(Tile(
                    (x * tile_size, y * tile_size),
                    spritesheet[tile]
                ))
            elif tile != 'empty':
                print('Error, wrong tile')

            x += 1
            if x == width:
                y += 1
                x = 0
            if y == height:
                break

    return Level(player_pos, tiles, None)


def load():
    path = 'level/levels'
    filenames = os.listdir(path)
    filenames.sort()
    levels = []
    for filename in filenames:
        with open(path + '/' + filename, 'r') as file:
            levels.append(parse_level(file.readlines()))

    return levels

levels = load()