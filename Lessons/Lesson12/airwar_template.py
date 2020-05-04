# Fly a jet thru a missile barrage

import pygame
import random

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SKY_BLUE = (135, 206, 250)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# load the images

# Define the Player object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite

# Define the enemy object extending pygame.sprite.Sprite
# Instead of a surface, we use an image for a better looking sprite

# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite

# Create custom events for adding a new enemy and cloud

# Create our 'player'

# Create groups to hold enemy sprites, cloud sprites, and all sprites
# - enemies is used for collision detection and position updates
# - clouds is used for position updates
# - all_sprites isused for rendering

# Variable to keep our main loop running
RUNNING = True

# Our main loop
while RUNNING:
    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == pygame.KEYDOWN:
            # Was it the Escape key? If so, stop the loop
            if event.key == pygame.K_ESCAPE:
                RUNNING = False

        # Did the user click the window close button? If so, stop the loop
        elif event.type == pygame.QUIT:
            RUNNING = False

    # Get the set of keys pressed and check for user input

    # Update the position of our enemies and clouds

    # Fill the screen with sky blue

    # Draw all our sprites

    # Check if any enemies have collided with the player

    # Flip everything to the display
    pygame.display.flip()

    # Ensure we maintain a 30 frames per second rate
    clock.tick(30)

pygame.quit()