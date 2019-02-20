import pygame

def xD(number):
    number += 1

class Ship():

    def __init__(self, shipSetting, screen):
        self.screen = screen

        self.shipSetting = shipSetting

        self.image = pygame.image.load("../images/spaceship.bmp")

        self.image_resolution = (45, 60)
        self.image = pygame.transform.scale(self.image, self.image_resolution)

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.shipSetting.speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.shipSetting.speed_factor

        self.rect.centerx = self.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)