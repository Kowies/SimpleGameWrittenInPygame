from pygame.sprite import Group

from bullet import Bullet

class Bullets(Group):

    def __init__(self, bullets_settings, ship, screen):
        super().__init__()

        self.__bullets_settings = bullets_settings
        self.__ship = ship

        self.__screen_surface_rect = screen.surface.get_rect()

        #number of bullets on the screen at this time
        self.amount_of_bullets = 0

    def shoot(self):
        if self.amount_of_bullets < self.__bullets_settings.max_amount:
            new_bullet = Bullet(self.__bullets_settings.bullet_settings,
                self.__ship)
            self.add(new_bullet)
            self.amount_of_bullets += 1

    def update(self):
        for bullet in self.sprites():
            bullet.update()
            if bullet.rect.bottom < self.__screen_surface_rect.top:
                self.remove(bullet)
                self.amount_of_bullets -= 1


