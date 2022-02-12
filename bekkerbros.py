#!/usr/bin/env python3

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Bekker Bros')
clock = pygame.time.Clock()
test_font = pygame.font.Font('src/font/pixeltype.ttf', 50)

game_active = True

sky_surface = pygame.image.load('src/graphics/sky.png').convert()
ground_surface = pygame.image.load('src/graphics/ground.png').convert()
text_surface = test_font.render('Welcome to BekkerBros', False, (64,64,64))
score_rectangle = text_surface.get_rect(center = (400, 50))

bro_surface = pygame.image.load('src/graphics/character_pixelated.png').convert_alpha()
bro_rectangle = bro_surface.get_rect(bottomright=(600,300)) # where do we place the rectangle

player_surface = pygame.image.load('src/graphics/enemies/monster_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80,300))
player_gravty = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                player_gravty = -25

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:
                player_gravty = -25

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        pygame.draw.rect(screen,'#c0e8ec',score_rectangle)
        pygame.draw.rect(screen,'#c0e8ec',score_rectangle,10)
        screen.blit(text_surface,score_rectangle)

        bro_rectangle.x -= 4
        if bro_rectangle.right < 0: bro_rectangle.left = 800
        screen.blit(bro_surface,bro_rectangle)

        # Player
        player_gravty += 1
        player_rectangle.y += player_gravty
        if player_rectangle.bottom >= 300: player_rectangle.bottom = 300
        screen.blit(player_surface,player_rectangle)

        # Collisions
        if bro_rectangle.colliderect(player_rectangle):
            print('collision detected, game over')
            game_active = False
    
    else:
        screen.fill('Black')

    pygame.display.update()
    clock.tick(60)

