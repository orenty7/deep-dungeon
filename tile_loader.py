import pygame


def load(path, source_size):
    with open(path) as f:
        spritesheet = pygame.image.load(f)

    spritesheets = []
    for y in range(spritesheet.get_height() // source_size):
        spritesheets.append([])
        for x in range(spritesheet.get_width() // source_size):
            sprite_image = spritesheet.subsurface(x * source_size, y * source_size, source_size, source_size)
            spritesheets[y].append(sprite_image)

    return spritesheets


def trim_sprite(sprite):
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

    return sprite.subsurface(bound_min_x, bound_min_y, bound_max_x - bound_min_x, bound_max_y - bound_min_y)


def scale(sprites, size):
    for y in range(len(sprites)):
        for x in range(len(sprites[y])):
            sprites[y][x] = pygame.transform.scale(sprites[y][x], (size, size))


tmp = load('sprites/sheet.png', 16)
tmp = tmp[:-1:]
sprites = []
for row in tmp:
    sprites.append(row[7::])

scale(sprites, 64)

characters = load('sprites/characters.png', 32)
scale(characters, 128)

x = 0
if __name__ == '__main__':
    sprites = characters
    pygame.init()
    screen = pygame.display.set_mode((128 * (len(sprites[0])), 128 * (len(sprites))))
    clock = pygame.time.Clock()

    finished = False
    while not finished:
        screen.fill('white')
        for y in range(len(sprites)):
            for x in range(len(sprites[y])):
                screen.blit(sprites[y][x], (128 * x, 128 * y))
                pygame.draw.rect(screen, 'black', ((128 * x, 128 * y), (128, 128)), 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        pygame.display.update()
        clock.tick(1)
