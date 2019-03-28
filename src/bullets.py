import collections

from pygame.sprite import Group

from bullet import Bullet


class Bullets(Group):

    def __init__(self, bullets_settings, ship, screen):
        self.__bullets_settings = bullets_settings
        self.__ship = ship

        self.__screen_surface_rect = screen.surface.get_rect()

        #number of bullets on the screen at this time
        self.amount_of_bullets = 0
        super().__init__()

    def shoot(self):
        if self.amount_of_bullets < self.__bullets_settings.max_amount:
            new_bullet = Bullet(self.__bullets_settings.bullet_settings,
                self.__ship)
            self.add(new_bullet)

    def update(self):
        for bullet in self.sprites():
            bullet.update()
            if bullet.rect.bottom < self.__screen_surface_rect.top:
                self.remove(bullet)

    def add(self, *sprites):
        amout_of_spirtes = 0

        for sprite in sprites:
            if isinstance(sprite, collections.Iterable):
                amout_of_spirtes += len(sprite)
            else:
                amout_of_spirtes += 1

        self.amount_of_bullets += amout_of_spirtes

        super().add(*sprites)

    def remove(self, *sprites):
        amout_of_spirtes = 0

        for sprite in sprites:
            if isinstance(sprite, collections.Iterable):
                amout_of_spirtes += len(sprite)
            else:
                amout_of_spirtes += 1

        self.amount_of_bullets -= amout_of_spirtes

        super().remove(*sprites)