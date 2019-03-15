import pygame

from settings import GameSettings
from screen import Screen
from ship import Ship
from bullets import Bullets
from event_checker import EventChecker

from dvd_logo import DVDLogo
from settings import DVDLogoSettings

class SimpleGameWrittenInPygame():

    def __init__(self):
        self.__game_settings = GameSettings()
        self.__screen = Screen(self.__game_settings.screen_settings)
        self.__ship = Ship(self.__game_settings.ship_settings, self.__screen)

        self.__bullets = Bullets(self.__game_settings.bullets_settings, 
            self.__ship, self.__screen)

        self.__event_checker = EventChecker(self.__game_settings, 
            self.__ship, self.__bullets)

    def run_game(self):
        pygame.init()

        rect = self.__screen.surface.get_rect()
        center = [rect.centerx, rect.centery]

        dvd_logo = DVDLogo(DVDLogoSettings(), center, [0.1,0.1] )

        to_update = [self.__ship, self.__bullets, dvd_logo]
        to_draw = [self.__ship, self.__bullets, dvd_logo]
        screen_surface = self.__screen.surface

        while True:
            self.__event_checker.check_events()

            self.__screen.update()
            for x in to_update:
                x.update()
            for x in to_draw:
                x.draw(screen_surface)
            self.__screen.flip()

            print(len(self.__bullets))

if __name__ == "__main__":
    game = SimpleGameWrittenInPygame()
    game.run_game() 