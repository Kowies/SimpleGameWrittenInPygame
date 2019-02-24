import pygame

from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, gameSettings, screen):
        super().__init__()

        self.gameSettings = gameSettings
        self.screen = screen

        self.image = pygame.image.load("../images/alien.bmp")
        self.image_resolution = (self.gameSettings.alienSettings.width,
            self.gameSettings.alienSettings.height)
        self.image = pygame.transform.scale(self.image, self.image_resolution)
        
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)