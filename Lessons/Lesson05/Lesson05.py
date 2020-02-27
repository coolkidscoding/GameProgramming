# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:00:14 2020

@author: jrizos

Pygame template - Starting point for our pygame development
"""

import pygame
import random
#6 import os

# set up asset folders
#6 game_folder = os.path.dirname(__file__)
#7 image_folder = os.path.join(game_folder, 'image')
#7 player_img = pygame.image.load(os.path.join(image_folder, 'p1_jump.png')).convert()

WIDTH = 800
HEIGHT = 570
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# create our Player
#2class Player(pygame.sprite.Sprite):
#2    def __init__(self):
#2        pygame.sprite.Sprite.__init__(self)
#2        self.image = pygame.Surface((50,50))
#8        self.image = player_img
#10       self.set_colorkey(BLACK)
#2        self.image.fill(GREEN)
#2        self.rect = self.image.get_rect()
#2        self.rect.center = (WIDTH/2, HEIGHT/2)

#4def update(self):
#4    self.rect.x += 5
#5    if self.rect.left > WIDTH:
#5       self.rect.right = 0

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My PyGame")
clock = pygame.time.Clock()
#1 all_sprites = pygame.sprite.Group()
#3 player = Player()
#3 all_sprites.add(player)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    #1 all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    #9 screen.fill(BLUE)
    #1 all_sprites.draw(screen)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

