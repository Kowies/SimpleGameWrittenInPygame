from pygame.sprite import groupcollide

class CollisionDetector():

    def __init__(self, collison_detector_settings, ship, bullets, dvd_logos):
        self.__collison_detector_settings = collison_detector_settings
        self.__ship = ship
        self.__bullets = bullets
        self.__dvd_logos = dvd_logos


    def update(self):
        sprite_dict = groupcollide(self.__bullets, self.__dvd_logos, False, False)
        self.__bullets.remove(sprite_dict.keys())