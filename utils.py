import pygame


def check_side_y(sprite, rng_x, rng_y):
    for y in rng_y:
        for x in rng_x:
            if sprite.get_at((x, y)) != (255, 255, 255, 0):
                return y
    return None


def check_side_x(sprite, rng_x, rng_y):
    for x in rng_x:
        for y in rng_y:
            if sprite.get_at((x, y)) != (255, 255, 255, 0):
                return x
    return None


def hitbox(sprite):
    tmp = check_side_y(sprite, range(sprite.get_width()), range(sprite.get_height()))
    bound_min_y = tmp if tmp is not None else 0

    tmp = check_side_y(sprite, range(sprite.get_width()), reversed(range(sprite.get_height())))
    bound_max_y = tmp if tmp is not None else sprite.get_height()

    tmp = check_side_x(sprite, range(sprite.get_width()), range(sprite.get_height()))
    bound_min_x = tmp if tmp is not None else 0

    tmp = check_side_x(sprite, reversed(range(sprite.get_width())), range(sprite.get_height()))
    bound_max_x = tmp if tmp is not None else sprite.get_width()

    return (bound_min_x, bound_min_y), (bound_max_x - bound_min_x, bound_max_y - bound_min_y)


def center(surface, rect):
    rect_size = rect.size
    rect_pos = rect.topleft
    size = surface.get_size()

    pos = [*rect_pos]

    pos[0] += (rect_size[0] - size[0]) / 2
    pos[1] += (rect_size[1] - size[1]) / 2

    return pos


def button_rect(size, i, params):
    offset_x = (size[0] - params['width'] * params['buttons in row'] - params['padding x'] * (
            params['buttons in row'] - 1)) / 2
    offset_y = size[1] // 5

    y = i // params['buttons in row']
    x = i % params['buttons in row']
    return pygame.Rect(offset_x + (params['width'] + params['padding x']) * x,
                       offset_y + (params['height'] + params['padding y']) * y, params['width'], params['height'])
