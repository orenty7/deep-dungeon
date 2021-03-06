import os

from settings import tile_size
from tiles import spritesheet, Tile, TileEnd, TileKill
from .level import Level


def parse_level(lines):
    lines = list(filter(lambda s: s != '', map(str.strip, lines)))
    width, height = list(map(int, lines[0].split()))
    player_pos = list(map(int, lines[1].split()))

    tiles_str = map(str.split, lines[2::])

    x, y = (0, 0)
    tiles = []
    for line in tiles_str:
        for tile in line:
            if tile in spritesheet:
                if tile != 'water':
                    tiles.append(Tile(
                        (x * tile_size, y * tile_size),
                        spritesheet[tile]
                    ))
                else:
                    tiles.append(TileKill(
                        (x * tile_size, y * tile_size),
                        spritesheet[tile]
                    ))
            elif tile == 'invisible':
                tiles.append(Tile((x * tile_size, y * tile_size)))
            elif tile == 'end':
                tiles.append(TileEnd((x * tile_size, y * tile_size)))
            elif tile != 'empty':
                print('Error, wrong tile')

            x += 1
            if x == width:
                y += 1
                x = 0
            if y == height:
                break

    return Level(player_pos, tiles)


def load():
    path = 'level/levels'
    filenames = os.listdir(path)
    filenames.sort()
    levels = []
    for filename in filenames:
        if filename[0] == '_':
            continue
        with open(path + '/' + filename, 'r') as file:
            levels.append(parse_level(file.readlines()))

    return levels


levels = load()
