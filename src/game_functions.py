import sys

import pygame

import settings

from bullet import Bullet


def check_keydown_events(event, gameSettings, screen, ship,  bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

    if event.key == pygame.K_SPACE:

        bullets_allowed = gameSettings.bulletSettings.bullets_allowed
        if bullets_allowed > len(bullets):
            new_bullet = Bullet(gameSettings.bulletSettings, screen, ship)
            bullets.add(new_bullet)
            

def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(gameSettings, screen, ship,  bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, gameSettings, screen, ship,  bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(screenSettings, screen, ship, bullets):
    screen.fill(screenSettings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw()

    ship.blitme()

    pygame.display.flip()


def update_bullets(bullets):

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)