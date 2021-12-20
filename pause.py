import pygame

from settings import BACKGROUND_COLOR, COLOR
from utils import button_rect, center


class Pause:
    blitting_params = {
        'padding x': 100,
        'padding y': 20,
        'width': 300,
        'height': 70,
        'buttons in row': 1
    }

    def __init__(self, options):
        self.options = options
        self.surfaces = [None] * len(options)
        self.render_text()

    def render_text(self):
        font = pygame.font.Font('DisposableDroidBB_bld.ttf', 50)

        for i in range(len(self.options)):
            self.surfaces[i] = font.render(self.options[i], False, COLOR, BACKGROUND_COLOR)

    def tick(self, screen, events):
        screen.fill(BACKGROUND_COLOR)
        size = screen.get_size()
        for i in range(len(self.surfaces)):
            rect = button_rect(size, i, self.blitting_params)
            pygame.draw.rect(screen, COLOR, rect, 5)
            screen.blit(self.surfaces[i], center(self.surfaces[i], rect))

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.surfaces)):
                    if button_rect(size, i, self.blitting_params).collidepoint(event.pos):
                        return self.options[i]
