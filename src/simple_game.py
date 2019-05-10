import pygame

from settings import GameSettings
from screen import Screen
from ship import Ship
from bullets import Bullets
from dvd_logos import DVDLogos
from collision_detector import CollisionDetector
from event_checker import EventChecker



class SimpleGameWrittenInPygame():

    def __init__(self):
        self.__game_settings = GameSettings()
        self.__screen = Screen(self.__game_settings.screen_settings)
        self.__ship = Ship(self.__game_settings.ship_settings, self.__screen)

        self.__bullets = Bullets(self.__game_settings.bullets_settings, 
            self.__ship, self.__screen)

        self.__dvd_logos = DVDLogos(self.__game_settings.dvd_logos_settings, 
            self.__ship, self.__screen)

        self.__collison_detector = CollisionDetector(
            self.__game_settings.collison_detector_settings, self.__ship,
            self.__bullets, self.__dvd_logos)

        self.__event_checker = EventChecker(self.__game_settings, 
            self.__ship, self.__bullets)


    def run_game(self):
        pygame.init()

        to_update = [self.__collison_detector, self.__ship, self.__bullets, 
            self.__dvd_logos]
        to_draw = [self.__ship, self.__bullets, self.__dvd_logos]
        screen_surface = self.__screen.surface

        self.__dvd_logos.create(15)

        while True:
            self.__event_checker.check_events()

            self.__screen.update()
            for x in to_update:
                x.update()
            for x in to_draw:
                x.draw(screen_surface)
            self.__screen.flip()

            if self.__dvd_logos.is_any_logo() != True:
                print("YOU WIN! :D")
                return 0
            if self.__collison_detector.ship_was_hit():
                print("YOU LOSE! :<")
                return 0


if __name__ == "__main__":
    game = SimpleGameWrittenInPygame()
    game.run_game() 