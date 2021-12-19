def load(path):
    sprites = {
        'stone-grass-right': (0, 2),
        'stone-grass-center': (1, 2),
        'stone-grass-left': (2, 2),
        'stone-break-left': (3, 2),
        'stone-center': (4, 2),
        'stone-break-right': (5, 2),
        'stone-middle': (6, 2),
        'under-stone': (0, 3),
        'stone-break-grass-right': (1, 3),
        'stone-break-grass-left': (2, 3),
        'under-stone-left': (3, 3),
        'grass': (4, 3),
        'under-stone-right': (5, 3),
        'under-stone-center': (6, 3),
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
