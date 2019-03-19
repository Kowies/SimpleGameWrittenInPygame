import random

from pygame.sprite import Group
from pygame import Rect

from dvd_logo import DVDLogo

class DVDLogos(Group):

    def __init__(self, dvd_logos_settings, ship, screen):
        super().__init__()

        self.__dvd_logos_settings = dvd_logos_settings
        self.__ship = ship

        self.__screen_surface_rect = screen.surface.get_rect()

        self.__screen_surface_rect_allowed = self.__screen_surface_rect

        self.__screen_surface_rect_allowed.bottom //= 2

        dvd_logo_settings = self.__dvd_logos_settings.dvd_logo_settings
        self.__logo_resolution = dvd_logo_settings.image_resolution

        self.__screen_surface_rect_allowed.bottom -= logo_resolution[1]
        self.__screen_surface_rect_allowed.top += logo_resolution[1]

        self.__screen_surface_rect_allowed.right -= logo_resolution[0]
        self.__screen_surface_rect_allowed.left += logo_resolution[0] 

        self.__number_of_logos = 0

    @staticmethod
    def rand_vector():
        return (random.random(), random.random())

    def rand_rect_which_allowed(self):
        rect = Rect((0, 0), self.__logo_resolution)

        left = self.__screen_surface_rect_allowed.left
        right = self.__screen_surface_rect_allowed.right
        top = self.__screen_surface_rect_allowed.top
        bottom = self.__screen_surface_rect_allowed.bottom

        rect.centerx = random.randrange(left, right)
        rect.centery = random.randrange(top, bottom)

    def create(self, number=5):

        for i in range(number):
            rect = self.rand_rect_which_allowed()
            vector = self.rand_vector()

            dvd_logo_settings = self.__dvd_logos_settings.dvd_logo_settings
            new_dvd_logo = DVDLogo(dvd_logo_settings, )


    def update(self):
        for bullet in self.sprites():
            bullet.update()
            if bullet.rect.bottom < self.__screen_surface_rect.top:
                self.remove(bullet)
                self.amount_of_bullets -= 1


