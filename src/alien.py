import pygame

from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, game_settings, screen):
        super().__init__()

        self.game_settings = game_settings
        self.screen = screen

        self.image = pygame.image.load("../images/alien.bmp")
        self.image_resolution = (self.game_settings.alien_settings.width,
            self.game_settings.alien_settings.height)
        self.image = pygame.transform.scale(self.image, self.image_resolution)
        
        self.rect = self.image.get_rect()

        self.rect.x  = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    # def blitme(self):
    #     self.screen.blit(self.image, self.rect)