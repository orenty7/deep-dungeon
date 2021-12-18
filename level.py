from tiles import Tile
level = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [(0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1), (0, 1)],
    [(1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4)],
    [(1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4),
     (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4)],
    [(1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4),
     (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4)],
    [(1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4),
     (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4), (1, 4)],

]

tiles = []
for y in range(len(level)):
    for x in range(len(level[y])):
        tiles.append(Tile(
            ((64 * x, 64 * y), (64, 64)),
            level[y][x]
        ))

