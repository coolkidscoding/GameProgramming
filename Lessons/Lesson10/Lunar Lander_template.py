# Lunar Lander
# simulation game of landing a spacecraft

# initialize - get everything ready
import pygame

# setup constants
WIDTH = 400
HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_GREY = (128, 128, 128)
DARK_GREY = (60, 60, 60)
FLAME = (255, 109, 14)

FPS = 30

# setup the screen
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lunar Lander')
clock = pygame.time.Clock()

screen.fill(BLACK)

# setup some game variables
# used to control the ships descent

# main loop
RUNNING = True
while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_held_down = True
            print('mouse button down')
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_held_down = False
            print('mouse button up')
        elif event.type == pygame.MOUSEMOTION:
            if mouse_held_down:
                print('mouse move')
                myThrottle.rect.centery = event.pos[1]
                if myThrottle.rect.centery < 300:
                    myThrottle.rect.centery = 300
                if myThrottle.rect.centery > 500:
                    myThrottle.rect.centery = 500

pygame.quit()
# End of File
