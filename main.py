import pygame

from enums import WindowState
from level import levels
from menu import Menu
from pause import Pause
from settings import FPS
from utils import center

window = (64 * 20, 64 * 12)

pygame.init()
screen = pygame.display.set_mode(window)
clock = pygame.time.Clock()

timer = 0

font = pygame.font.Font('DisposableDroidBB_bld.ttf', 50)
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
                finished = True
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
    elif state == WindowState.Game:
        level.tick(screen, events)
        game_result = level.is_won()
        if game_result is not None:
            state = WindowState.GameOver
            timer = 1 * FPS
            if game_result:
                text = font.render("You Win", False, 'white')
            else:
                text = font.render("You Lose", False, 'white')
    elif state == WindowState.GameOver:
        timer -= 1
        screen.fill('black')
        screen.blit(text, center(text, screen.get_rect()))

        if timer == 0:
            state = WindowState.MainMenu
    else:
        raise Exception('Incorrect state')
    pygame.display.update()
