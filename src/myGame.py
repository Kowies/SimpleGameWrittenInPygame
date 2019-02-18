import pygame

from settings import Settings
from ship import Ship
import game_functions

def run_game():

    pygame.init()
    pygame.display.set_caption("myGame")

    settings = Settings()
    screen = pygame.display.set_mode( (settings.screen_width, settings.screen_height) )
    ship = Ship(screen)

    while True:
        game_functions.check_events()
        game_functions.update_screen(settings, screen, ship)


run_game()
