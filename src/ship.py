import pygame

class Ship():

    def __init__(self, game_settings, screen):
        self.screen_surface = screen.surface

        self.ship_settings = game_settings.ship_settings

        self.image = pygame.image.load("../images/spaceship.bmp")

        self.image_resolution = (45, 60)
        self.image = pygame.transform.scale(self.image, self.image_resolution)

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen_surface.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.centerx = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False


    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ship_settings.speed_factor

        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.centerx -= self.ship_settings.speed_factor

        self.rect.centerx = self.centerx

    def draw(self):
        self.screen_surface.blit(self.image, self.rect)