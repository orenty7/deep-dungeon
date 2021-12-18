import pygame

sprite_width = 16
sprite_height = 16


def load():
    with open('sprites/sheet.png') as f:
        spritesheet = pygame.image.load(f)

    data = []
    spritesheets = []
    for y in range(spritesheet.get_height() // sprite_height):
        spritesheets.append([])
        for x in range(spritesheet.get_width() // sprite_width) :
            sprite_image = spritesheet.subsurface(x * sprite_width, y * sprite_height, sprite_width, sprite_height)
            spritesheets[y].append(pygame.transform.scale(sprite_image, (64, 64)))


    return spritesheets


def draw(screen):
    pass
