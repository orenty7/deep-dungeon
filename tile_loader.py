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




def scale(sprites, size):
    for y in range(len(sprites)):
        for x in range(len(sprites[y])):
            sprites[y][x] = pygame.transform.scale(sprites[y][x], (size, size))


tmp = load('tiles/sprites/sheet.png', 16)
tmp = tmp[:-1:]
sprites = []
for row in tmp:
    sprites.append(row[7::])

scale(sprites, 64)

characters = load('tiles/sprites/characters.png', 32)
scale(characters, 128)


x = 0
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((96 * (len(sprites[0])), 96 * (len(sprites))))
    clock = pygame.time.Clock()

    finished = False
    while not finished:
        screen.fill('white')
        for y in range(len(sprites)):
            for x in range(len(sprites[y])):
                screen.blit(sprites[y][x], (96 * x, 96 * y))
                pygame.draw.rect(screen, 'black', ((96 * x, 96 * y), (96, 96)), 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        pygame.display.update()
        clock.tick(120)
