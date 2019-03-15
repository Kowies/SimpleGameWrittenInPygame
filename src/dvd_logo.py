import pygame
from pygame.sprite import Sprite

from sklearn import preprocessing

class DVDLogo(Sprite):

    def __init__(self, dvdlogo_settings, center, vector):
        super().__init__()

        self.__dvdlogo_settings = dvdlogo_settings

        image_path = self.__dvdlogo_settings.image_path
        self.image = pygame.image.load(image_path)

        image_resolution = self.__dvdlogo_settings.image_resolution
        self.image = pygame.transform.scale(self.image, image_resolution)

        self.rect = self.image.get_rect()

        self.rect.centerx = center[0]
        self.rect.centery = center[1]

        self.__centerx = float(self.rect.centerx)
        self.__centery = float(self.rect.centery)

        vector_normalized = vector #todo
        self.vector = vector_normalized
        self.vector *= self.__dvdlogo_settings.speed_factor

    def update(self):
        self.__centerx += self.vector[0]
        self.__centery += self.vector[1]

        self.rect.centerx = self.__centerx
        self.rect.centery = self.__centery
        

    def draw(self, screen_surface):
        screen_surface.blit(self.image, self.rect)

