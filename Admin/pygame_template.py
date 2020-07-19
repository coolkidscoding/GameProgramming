# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 12:00:14 2020

@author: jrizos

Pygame template - Starting point for our pygame development
"""

import pygame
import random

WIDTH = 800
HEIGHT = 570
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My PyGame")
clock = pygame.time.Clock()

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

    # Draw / render
    screen.fill(BLACK)

    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()

