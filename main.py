from engine import Engine
from enums import Key
from level import levels
from player import Player
from tile_loader import *

level = levels[0]
level.init_engine((64 * 20, 64 * 12))

FPS = 120

pygame.init()
screen = pygame.display.set_mode((64 * 20, 64 * 12))
clock = pygame.time.Clock()

finished = False
while not finished:
    clock.tick(FPS)

    screen.fill('white')
    level.engine.tick(1 / FPS)
    level.engine.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            print(event)
            if event.key == pygame.K_w:
                level.engine.keydown(Key.W)
            elif event.key == pygame.K_a:
                level.engine.keydown(Key.A)
            elif event.key == pygame.K_s:
                level.engine.keydown(Key.S)
            elif event.key == pygame.K_d:
                level.engine.keydown(Key.D)
            elif event.key == pygame.K_SPACE:
                level.engine.keydown(Key.Space)
        elif event.type == pygame.KEYUP:
            print(event)
            if event.key == pygame.K_w:
                level.engine.keyup(Key.W)
            elif event.key == pygame.K_a:
                level.engine.keyup(Key.A)
            elif event.key == pygame.K_s:
                level.engine.keyup(Key.S)
            elif event.key == pygame.K_d:
                level.engine.keyup(Key.D)
            elif event.key == pygame.K_SPACE:
                level.engine.keyup(Key.Space)

    pygame.display.update()
