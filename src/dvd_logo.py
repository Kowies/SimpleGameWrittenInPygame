import numpy as np

import pygame
from pygame.sprite import Sprite

class DVDLogo(Sprite):

    def __init__(self, dvd_logo_settings, screen, point, vector):
        super().__init__()

        self.__dvd_logo_settings = dvd_logo_settings

        image_path = self.__dvd_logo_settings.image_path
        self.image = pygame.image.load(image_path)

        image_resolution = self.__dvd_logo_settings.image_resolution
        self.image = pygame.transform.scale(self.image, image_resolution)
        self.change_color_to_rand()

        self.rect = self.image.get_rect()

        self.__screen_surface_rect = screen.surface.get_rect()

        self.rect.centerx = point[0]
        self.rect.centery = point[1]

        self.__centerx = float(self.rect.centerx)
        self.__centery = float(self.rect.centery)

        vector = np.array(vector)

        vector_normalized = vector / (vector**2).sum() ** 0.5
        self.vector = vector_normalized
        self.vector *= self.__dvd_logo_settings.speed_factor

    def change_color(self, color):
        surface = self.image
        w, h = surface.get_size()
        r, g, b = color
        for x in range(w):
            for y in range(h):
                a = surface.get_at((x, y))[3]
                surface.set_at((x, y), pygame.Color(r, g, b, a))


    def change_color_to_rand(self):
        color = tuple((np.random.rand(3) * 256).astype(int) )
        color = [int(x) for x in color]
        self.change_color(color)


    def update(self):
        self.__centerx += self.vector[0]
        self.__centery += self.vector[1]

        self.rect.centerx = self.__centerx
        self.rect.centery = self.__centery

        if self.rect.bottom >= self.__screen_surface_rect.bottom:
            self.vector[1] *= -1
            self.change_color_to_rand()

        if self.rect.top <= self.__screen_surface_rect.top:
            self.vector[1] *= -1
            self.change_color_to_rand()

        if self.rect.left <= self.__screen_surface_rect.left:
            self.vector[0] *= -1
            self.change_color_to_rand()

        if self.rect.right >= self.__screen_surface_rect.right:
            self.vector[0] *= -1
            self.change_color_to_rand()


    def draw(self, screen_surface):
        screen_surface.blit(self.image, self.rect)

