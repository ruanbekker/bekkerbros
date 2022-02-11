#!/usr/bin/env python3

import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Bekker Bros')
clock = pygame.time.Clock()
test_font = pygame.font.Font('src/font/pixeltype.ttf', 50)

sky_surface = pygame.image.load('src/graphics/sky.png').convert()
ground_surface = pygame.image.load('src/graphics/ground.png').convert()
text_surface = test_font.render('Welcome to BekkerBros', False, 'Black')

bro_surface = pygame.image.load('src/graphics/character_pixelated.png').convert_alpha()
#bro_x_pos = 600
bro_rectangle = bro_surface.get_rect(bottomright=(600,300)) # where do we place the rectangle

player_surface = pygame.image.load('src/graphics/enemies/monster_walk_1.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(230,50))
    # get position
    #print(player_rectangle.left)
    bro_rectangle.x -= 4
    if bro_rectangle.right < 0: bro_rectangle.left = 800
    screen.blit(bro_surface,bro_rectangle)
    screen.blit(player_surface,player_rectangle)

    if player_rectangle.colliderect(bro_rectangle):
        print('collision')

    #if player_rectangle.collidepoint((x,y)):


    pygame.display.update()
    clock.tick(60)
