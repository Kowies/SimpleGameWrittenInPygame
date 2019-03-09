import pygame

class Screen():

    def __init__(self, game_settings):

        self.__game_settings = game_settings
        screen_settings = self.__game_settings.screen_settings

        self.__bg_color = screen_settings.bg_color
        pygame.display.set_caption(screen_settings.caption)

        resolution = (screen_settings.width, screen_settings.height)
        self.surface = pygame.display.set_mode(resolution)

    def update(self):
        self.surface.fill(self.__bg_color)

    def draw(self):
        pygame.display.flip()