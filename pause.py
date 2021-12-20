import pygame


class Pause:
    def __init__(self, options, window, width):
        self.options = {}
        for option in options:
            self.options[option] = {}
            self.options[option]['surface'] = None
            self.options[option]['callbacks'] = []

        self.render_text()

    def render_text(self):
        font = pygame.font.Font('DisposableDroidBB_bld.ttf', 50)

        for option in self.options.keys():
            self.options[option]['surface'] = font.render(option, False, 'black')

    def click(self, event):
        pass

    def onclick(self, option, callback):
        self.options[option]['callbacks'].append(callback)

    def tick(self, screen, events):
        screen.fill('white')
        for i in range(len(self.options)):
            option = list(self.options.keys())[i]
            screen.blit(self.options[option]['surface'], (100, i * 70))
