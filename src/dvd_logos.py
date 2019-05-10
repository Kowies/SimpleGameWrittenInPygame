import random
import collections

from pygame.sprite import Group
from pygame import Rect

from dvd_logo import DVDLogo

class DVDLogos(Group):

    def __init__(self, dvd_logos_settings, ship, screen):
        super().__init__()

        self.__dvd_logos_settings = dvd_logos_settings
        self.__ship = ship

        self.__screen = screen

        self.__allowed_rect_for_spawn = self.designate_allowed_rect()

        self.__number_of_logos = 0


    def designate_allowed_rect(self):
        screen_surface_rect = self.__screen.surface.get_rect()

        left = screen_surface_rect.left
        right = screen_surface_rect.right
        top = screen_surface_rect.top
        bottom = screen_surface_rect.bottom

        bottom //= 2

        dvd_logo_settings = self.__dvd_logos_settings.dvd_logo_settings
        logo_resolution = dvd_logo_settings.image_resolution

        bottom -= logo_resolution[1]
        top += logo_resolution[1]

        right -= logo_resolution[0]
        left += logo_resolution[0]

        widht = right - left
        height = bottom - top

        return Rect((left, top), (widht, height))

    @staticmethod
    def rand_vector():
        return (random.random(), random.random())

    def rand_point_which_allowed(self):
        point = [0, 0]
        left = self.__allowed_rect_for_spawn.left
        right = self.__allowed_rect_for_spawn.right
        top = self.__allowed_rect_for_spawn.top
        bottom = self.__allowed_rect_for_spawn.bottom

        point[0] = random.randrange(left, right)
        point[1] = random.randrange(top, bottom)
        return point

    def create(self, number=5):
        for i in range(number):
            point = self.rand_point_which_allowed()
            vector = self.rand_vector()

            dvd_logo_settings = self.__dvd_logos_settings.dvd_logo_settings

            new_dvd_logo = DVDLogo(dvd_logo_settings, self.__screen, 
                point, vector)
            self.add(new_dvd_logo)
            self.__number_of_logos += 1

    def is_any_logo(self):
        if self.__number_of_logos > 0:
            return True
        return False

    # DONT WORK PROPERLY !!!
    def remove(self, *sprites):
        amout_of_spirtes = 0

        for sprite in sprites:
            if isinstance(sprite, collections.Iterable):
                amout_of_spirtes += len(sprite)
            else:
                amout_of_spirtes += 1

        self.__number_of_logos -= amout_of_spirtes

        super().remove(*sprites)

    def update(self):
        for dvd_logo in self.sprites():
            dvd_logo.update()



