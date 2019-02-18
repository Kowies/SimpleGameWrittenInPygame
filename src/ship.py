import pygame

def xD(number):
    number += 1

class Ship():

    def __init__(self, screen):



        self.screen = screen

        self.image = pygame.image.load("../images/spaceship.bmp")

        self.image_resolution = (30, 30)
        self.image = pygame.transform.scale(self.image, self.image_resolution)

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        self.screen.blit(self.image, self.rect)