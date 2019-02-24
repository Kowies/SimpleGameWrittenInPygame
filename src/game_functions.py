import sys

import pygame

import settings

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, gameSettings, screen, ship,  bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

    if event.key == pygame.K_SPACE:
        fire_bullet(gameSettings, screen, ship, bullets)

    if event.key == pygame.K_q:
        sys.exit()
        

def fire_bullet(gameSettings, screen, ship, bullets):
    bullets_allowed = gameSettings.bulletSettings.bullets_allowed   
    if (len(bullets) < bullets_allowed):
        newBullet = Bullet(gameSettings.bulletSettings, screen, ship)
        bullets.add(newBullet)


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

def update_screen(screenSettings, screen, ship, aliens, bullets):
    screen.fill(screenSettings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw()

    aliens.draw(screen)

    ship.blitme()
    
    pygame.display.flip()


def update_bullets(bullets):

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def createAlienFleet(gameSettings, screen, aliens):

    alien = Alien(gameSettings, screen)
    alienWidth = alien.rect.width
    availableSpaceX = gameSettings.screenSettings.width - 2 * alienWidth
    numberAliensX = int(availableSpaceX / (2 * alienWidth) )

    for alienNumber in range(numberAliensX):
        alien = Alien(gameSettings, screen)
        alien.x = alienWidth + 2 * alienWidth * alienNumber
        alien.rect.x = alien.x
        aliens.add(alien)
