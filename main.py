from engine import Engine
from enums import Key
from level import tiles
from player import Player
from tile_loader import *

player = Player((100, 100))

engine = Engine(tiles, player, {
    'gravity': 15
})
FPS = 120

pygame.init()
screen = pygame.display.set_mode((64 * 20, 64 * 12))
clock = pygame.time.Clock()

print(pygame.K_w)
print(pygame.K_a)
print(pygame.K_s)
print(pygame.K_d)

finished = False
while not finished:
    clock.tick(FPS)

    screen.fill('white')
    engine.tick(1 / FPS)
    engine.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.key == pygame.K_w:
                engine.keydown(Key.W)
            elif event.key == pygame.K_a:
                engine.keydown(Key.A)
            elif event.key == pygame.K_s:
                engine.keydown(Key.S)
            elif event.key == pygame.K_d:
                engine.keydown(Key.D)
            elif event.key == pygame.K_SPACE:
                engine.keydown(Key.Space)
        elif event.type == pygame.KEYUP:
            print(event)
            if event.key == pygame.K_w:
                engine.keyup(Key.W)
            elif event.key == pygame.K_a:
                engine.keyup(Key.A)
            elif event.key == pygame.K_s:
                engine.keyup(Key.S)
            elif event.key == pygame.K_d:
                engine.keyup(Key.D)
            elif event.key == pygame.K_SPACE:
                engine.keyup(Key.Space)

    pygame.display.update()
