import sys

import pygame


class EventChecker():

    def __init__(self, game_settings, ship, bullets):
        self.__game_settings = game_settings
        self.__ship = ship
        self.__bullets = bullets

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.__check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.__check_keyup_events(event)


    def __check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.__ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.__ship.moving_left = True

        if event.key == pygame.K_SPACE:
            self.__bullets.shoot()

        if event.key == pygame.K_q:
            sys.exit()

    def __check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.__ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.__ship.moving_left = False