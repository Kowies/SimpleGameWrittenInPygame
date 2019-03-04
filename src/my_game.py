import pygame

from pygame.sprite import Group

from settings import GameSettings
from ship import Ship
from alien import Alien

import game_functions

def run_game():

    pygame.init()
    pygame.display.set_caption("myGame")

    game_settings = GameSettings()
    screen_settings = game_settings.screen_settings
    ship_settings = game_settings.ship_settings

    screen = pygame.display.set_mode( (screen_settings.width, screen_settings.height) )
    ship = Ship(game_settings, screen)

    bullets = Group()

    aliens = Group()

    game_functions.create_alien_fleet(game_settings, screen, aliens)

    while True:
        game_functions.check_events(game_settings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(game_settings, screen, ship, aliens, bullets)

        print(len(bullets))


def main():
    run_game()

if __name__ == "__main__":
    main()