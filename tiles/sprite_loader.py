def load(path):
    sprites = {
        'water': (1, 5),
        'grass-right': (0, 0),
        'grass-center': (1, 0),
        'grass-left': (2, 0),
        'ground-right': (3, 0),
        'ground-center': (4, 0),
        'ground-left': (5, 0),
        'ground-middle': (6, 0),
        'underground': (0, 1),
        'grass-right-break': (1, 1),
        'grass-left-break': (2, 1),
        'underground-right': (3, 1),
        'underground-center': (4, 1),
        'underground-left': (5, 1),
        'underground-middle': (6, 1)

    }

    return sprites


spritesheet = load('tiles/sprites')
