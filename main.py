from engine import Engine
from tiles import Platform
from player import Player
from enums import Key

from tile_loader import *

import pygame

player = Player((100, 100, 60, 100))
tiles = []

for i in range(10):
    tiles.append(Platform((64 * i, 400 , 64, 64)))

for i in range(10):
    tiles.append(Platform((64 * 9, 400 + 64 * i , 64, 64)))


for i in range(5):
    tiles.append(Platform((64*15 + 64 * i, 400 , 64, 64)))

for i in range(10):
    tiles.append(Platform((64 * 15, 400 + 64 * i , 64, 64)))


engine = Engine(tiles, player, {
    'gravity': 15
})
FPS = 120

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

sprites = load()

print(pygame.K_w)
print(pygame.K_a)
print(pygame.K_s)
print(pygame.K_d)


finished = False
while not finished:
    clock.tick(FPS)

    screen.fill('white')
    engine.tick(1/FPS)
    engine.draw(screen)
    for y in range(len(sprites)):
        for x in range(8, len(sprites[y])):
            screen.blit(sprites[y][x], (x*64, y*64 + 64))
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

    pygame.display.update()
