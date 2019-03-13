import pygame

class Screen():

    def __init__(self, screen_settings):

        self.__screen_settings = screen_settings

        self.__bg_color = screen_settings.bg_color
        pygame.display.set_caption(screen_settings.caption)

        resolution = (screen_settings.width, screen_settings.height)
        self.surface = pygame.display.set_mode(resolution)

    def update(self):
        self.surface.fill(self.__bg_color)

    def flip(self):
        pygame.display.flip()