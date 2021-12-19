import pygame

def hitbox(sprite):
    bound_min_x = 0
    bound_min_y = 0
    bound_max_x = sprite.get_width()
    bound_max_y = sprite.get_height()

    found = False
    for y in range(sprite.get_height()):
        for x in range(sprite.get_width()):
            if sprite.get_at((x, y)) != (255, 255, 255, 0):
                bound_min_y = y
                found = True
        if found:
            break
    found = False
    for y in reversed(range(sprite.get_height())):
        for x in range(sprite.get_width()):
            if sprite.get_at((x, y)) != (255, 255, 255, 0):
                bound_max_y = y + 1
                found = True
        if found:
            break

    found = False
    for x in range(sprite.get_width()):
        for y in range(sprite.get_height()):
            if sprite.get_at((x, y)) != (255, 255, 255, 0):
                bound_min_x = x
                found = True
        if found:
            break

    found = False
    for x in reversed(range(sprite.get_width())):
        for y in range(sprite.get_height()):
            if sprite.get_at((x, y)) != (255, 255, 255, 0):
                bound_max_x = x + 1
                found = True
        if found:
            break

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
    offset_x = (size[0] - params['width'] * params['buttons in row'] - params['padding x'] * (params['buttons in row'] - 1)) / 2
    offset_y = size[1] // 5

    y = i // params['buttons in row']
    x = i % params['buttons in row']
    return pygame.Rect(offset_x + (params['width'] + params['padding x']) * x, offset_y + (params['height'] + params['padding y']) * y, params['width'], params['height'])
