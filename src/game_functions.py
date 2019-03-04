import sys

import pygame

import settings

from bullet import Bullet
from alien import Alien


def check_keydown_events(event, game_settings, screen, ship,  bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True

    if event.key == pygame.K_SPACE:
        fire_bullet(game_settings, screen, ship, bullets)

    if event.key == pygame.K_q:
        sys.exit()
        

def fire_bullet(game_settings, screen, ship, bullets):
    bullets_allowed = game_settings.bullet_settings.bullets_allowed   
    if len(bullets) < bullets_allowed:
        newBullet = Bullet(game_settings, screen, ship)
        bullets.add(newBullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(game_settings, screen, ship,  bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, game_settings, screen, ship,  bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(game_settings, screen, ship, aliens, bullets):
    screen.fill(game_settings.screen_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.draw()

    aliens.draw(screen)

    ship.draw()
    
    pygame.display.flip()


def update_bullets(bullets):

    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_alien_fleet(game_settings, screen, aliens):

    alien = Alien(game_settings, screen)
    alien_width = alien.rect.width
    available_space_x = game_settings.screen_settings.width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width) )

    for alien_number in range(number_aliens_x):
        alien = Alien(game_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)