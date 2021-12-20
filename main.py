import pygame

from level import levels
from settings import FPS
from enums import WindowState
from pause import Pause
from menu import Menu


window = (64 * 20, 64 * 12)

pygame.init()
screen = pygame.display.set_mode(window)
clock = pygame.time.Clock()

menu = Menu(levels)
pause = Pause(['resume', 'main menu'], window, 200)

finished = False
state = WindowState.MainMenu
while not finished:
    clock.tick(FPS)
    events = []
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if state == WindowState.Game:
                state = WindowState.Pause
            elif state == WindowState.Pause:
                state = WindowState.Game
            elif state == WindowState.MainMenu:
                state = WindowState.Game
        else:
            events.append(event)

    if state == WindowState.MainMenu:
        maybe_level = menu.tick(screen, events)
        if maybe_level is not None:
            level = maybe_level
            level.init_engine(window)
            state = WindowState.Game
    elif state == WindowState.Pause:
        pause.tick(screen, events)
    else:
        level.tick(screen, events)
        if level.is_end():
            state = WindowState.MainMenu
    pygame.display.update()




