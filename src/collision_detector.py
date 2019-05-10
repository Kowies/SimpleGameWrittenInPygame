from pygame.sprite import groupcollide, spritecollideany

class CollisionDetector():

    def __init__(self, collison_detector_settings, ship, bullets, dvd_logos):
        self.__collison_detector_settings = collison_detector_settings
        self.__ship = ship
        self.__bullets = bullets
        self.__dvd_logos = dvd_logos

    def ship_was_hit(self):
        if spritecollideany(self.__ship, self.__dvd_logos) == None:
            return False
        else:
            return True

    def update(self):
        sprite_dict = groupcollide(self.__bullets, self.__dvd_logos, False, True)

        self.__bullets.remove(*sprite_dict.keys())
        self.__dvd_logos.remove(*sprite_dict.keys()) # THIS SHOULDN'T LOOK LOOK LIKE THIS !!!
