import pygame

class Ship():

    def __init__(self, ship_settings, screen):

        self.__ship_settings = ship_settings

        image_path = self.__ship_settings.image_path
        self.image = pygame.image.load(image_path)

        image_resolution = self.__ship_settings.image_resolution
        self.image = pygame.transform.scale(self.image, 
            image_resolution)

        self.rect = self.image.get_rect()
        self.__screen_surface_rect = screen.surface.get_rect()

        self.rect.centerx = self.__screen_surface_rect.centerx
        self.rect.bottom = self.__screen_surface_rect.bottom

        self.__centerx = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.__screen_surface_rect.right:
            self.__centerx += self.__ship_settings.speed_factor

        if self.moving_left and self.rect.left > self.__screen_surface_rect.left:
            self.__centerx -= self.__ship_settings.speed_factor

        self.rect.centerx = self.__centerx

    def draw(self, screen_surface):
        screen_surface.blit(self.image, self.rect)