import pygame

from pygame.sprite import Group

from settings import GameSettings
from ship import Ship
import game_functions

def run_game():

    pygame.init()
    pygame.display.set_caption("myGame")

    gameSettings = GameSettings()
    screenSettings = gameSettings.screenSettings
    shipSettings = gameSettings.shipSettings

    screen = pygame.display.set_mode( (screenSettings.width, screenSettings.height) )
    ship = Ship(shipSettings, screen)

    bullets = Group()

    while True:
        game_functions.check_events(gameSettings, screen, ship, bullets)
        ship.update()
        game_functions.update_bullets(bullets)
        game_functions.update_screen(screenSettings, screen, ship, bullets)

        print(len(bullets))


def main():
    run_game()

if __name__ == "__main__":
    main()