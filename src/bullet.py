import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, game_settings, screen, ship):

        super().__init__()

        self.screen = screen
        self.ship = ship

        self.rect = pygame.Rect(0, 0, game_settings.bullet_settings.width,
            game_settings.bullet_settings.height)

        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.color = game_settings.bullet_settings.color
        self.speed_factor = game_settings.bullet_settings.speed_factor


    def update(self):

        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

        