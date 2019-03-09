import pygame

class Screen():

    def __init__(self, game_settings):

        self.game_settings = game_settings
        screen_settings = self.game_settings.screen_settings

        self.bg_color = screen_settings.bg_color
        pygame.display.set_caption(screen_settings.caption)

        resolution = (screen_settings.width, screen_settings.height)
        self.screen = pygame.display.set_mode(resolution)

    def update(self):
        self.screen.fill(self.bg_color)

    def draw(self):
        pygame.display.flip()