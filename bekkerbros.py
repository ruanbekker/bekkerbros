#!/usr/bin/env python3

from turtle import width
import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = test_font.render(f'Score: {current_time}', False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rectangle)
    return current_time

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Bekker Bros')
clock = pygame.time.Clock()
test_font = pygame.font.Font('src/font/pixeltype.ttf', 50)

game_active = False
start_time = 0
score = 0

# Background surfaces
sky_surface = pygame.image.load('src/graphics/sky.png').convert()
ground_surface = pygame.image.load('src/graphics/ground.png').convert()

# Text
# text_surface = test_font.render('Welcome to BekkerBros', False, (64,64,64))
# score_rectangle = text_surface.get_rect(center = (400, 50))

enemy_surface = pygame.image.load('src/graphics/character_pixelated.png').convert_alpha()
enemy_rectangle = enemy_surface.get_rect(bottomright=(600,300)) # where do we place the rectangle

player_surface = pygame.image.load('src/graphics/player/player_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80,300))
player_gravty = 0

# Intro screen
player_stand = pygame.image.load('src/graphics/player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rectangle = player_stand.get_rect(center = (400, 200))

game_name = test_font.render('BekkerBros', False, (111, 196, 169))
game_name_rectangle = game_name.get_rect(center = (400, 80))

game_message = test_font.render('Press Space to Start', False, (111, 196, 169))
game_message_rectangle = game_message.get_rect(center = (400, 320))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                    player_gravty = -25

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                    player_gravty = -25
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                enemy_rectangle.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        # pygame.draw.rect(screen,'#c0e8ec',score_rectangle)
        # pygame.draw.rect(screen,'#c0e8ec',score_rectangle,10)
        # screen.blit(text_surface,score_rectangle)
        score = display_score()

        enemy_rectangle.x -= 4
        if enemy_rectangle.right < 0: enemy_rectangle.left = 800
        screen.blit(enemy_surface, enemy_rectangle)

        # Player
        player_gravty += 1
        player_rectangle.y += player_gravty
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player_surface, player_rectangle)

        # Collisions
        if enemy_rectangle.colliderect(player_rectangle):
            print('collision detected, game over')
            game_active = False
    
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rectangle)

        score_message = test_font.render(f'Your Score: {score}', False, (111, 196, 169))
        score_message_rectangle = score_message.get_rect(center = (400, 330))
        screen.blit(game_name, game_name_rectangle)

        if score == 0:
            screen.blit(game_message, game_message_rectangle)
        else:
            screen.blit(score_message, score_message_rectangle)

    pygame.display.update()
    clock.tick(60)

