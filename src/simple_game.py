import pygame

from settings import GameSettings
from screen import Screen

class SimpleGameWrittenInPygame():

    def __init__(self):
        self.game_settings = GameSettings()
        self.screen = Screen(self.game_settings)

    def run_game(self):

        while True:
            self.screen.update()
            self.screen.draw()


if __name__ == "__main__":
    game = SimpleGameWrittenInPygame()
    game.run_game() 