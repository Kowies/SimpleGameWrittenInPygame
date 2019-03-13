import pygame

from settings import GameSettings
from screen import Screen
from ship import Ship
from event_checker import EventChecker

from bullet import Bullet #only for tests

class SimpleGameWrittenInPygame():

    def __init__(self):
        self.__game_settings = GameSettings()
        self.__screen = Screen(self.__game_settings.screen_settings)
        self.__ship = Ship(self.__game_settings.ship_settings, self.__screen)
        self.__event_checker = EventChecker(self.__game_settings, 
            self.__ship) 

    def run_game(self):
        pygame.init()
        
        bullet = Bullet(self.__game_settings.bullet_settings, self.__ship)
        to_update = [self.__ship]
        to_draw = [self.__ship]
        screen_surface = self.__screen.surface


        while True:
            self.__event_checker.check_events()

            self.__screen.update()
            for x in to_update:
                x.update()
            for x in to_draw:
                x.draw(screen_surface)
            self.__screen.flip()


if __name__ == "__main__":
    game = SimpleGameWrittenInPygame()
    game.run_game() 