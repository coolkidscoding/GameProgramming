#######################
# CKCS Game Programming
# Bullets
# 2020-04-24
#######################

import pygame

# Create some constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

# Create the sprites we need
# TBD

# Initialize the game
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Bullets')

clock = pygame.time.Clock()

# Create the sprite groups
# TBD

# Create the sprites
# TBD


# Define the game Loop
DONE = False

while not DONE:
    
    # process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            DONE = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # fire a bullet
            pass

    
    # define the game logic
    # TBD
    
    # clear the screen
    screen.fill(WHITE)

    # flip the display
    pygame.display.flip()

    # target 60 fps
    clock.tick(60)

pygame.quit()

# End of File
