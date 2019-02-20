import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, bulletSettings, screen, ship):

        super().__init__()

        self.screen = screen
        self.ship = ship

        self.rect = pygame.Rect(0, 0, bulletSettings.width, bulletSettings.height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = bulletSettings.color
        self.speed_factor = bulletSettings.speed_factor


    def update(self):

        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        