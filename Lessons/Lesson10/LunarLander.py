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

# landing pad is y = 540
ground = 540
start = 90

ship_mass = 5000.0
fuel = 5000.0
velocity = -100.0
gravity = 10
height = 2000
thrust = 0
delta_v = 0
y_pos = 90
mouse_held_down = False

# Load some graphic images we will use
ship = pygame.image.load('lunarlander.png')
moon = pygame.image.load('moonsurface.png')


# make the throttle
class ThrottleClass(pygame.sprite.Sprite):
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)
        image_surface = pygame.surface.Surface((30, 10))
        image_surface.fill(LIGHT_GREY)
        self.image = image_surface.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.centery = location

def draw_font(text_, fsize_, fcolor_, location_):
    font_obj = pygame.font.Font(None, fsize_)
    font_surf = font_obj.render(text_, 1, fcolor_)
    screen.blit(font_surf, location_)

# display the text with the speed, height, etc.
def display_stats():
    v_str = "velocity: %i m/s" % velocity
    h_str = "height:   %.1f" % height
    t_str = "thrust:   %i" % thrust
    a_str = "acceleration: %.1f" % (delta_v * FPS)
    f_str = "fuel:  %i" % fuel

    draw_font(v_str, 26, WHITE, (10, 50))
    draw_font(a_str, 26, WHITE, (10, 100))
    draw_font(h_str, 26, WHITE, (10, 150))
    draw_font(t_str, 26, WHITE, (10, 200))
    draw_font(f_str, 26, WHITE, (60, 300))

# display the ship's flames - size depends on the amount of thrust
def display_flames():
    flame_size = thrust / 15
    for i in range(2):
        startx = 252 - 10 + i * 19
        starty = y_pos + 83
        # the polygon is a triangle under each nozzle
        pygame.draw.polygon(screen, 
        FLAME, 
        [(startx, starty), (startx + 4, starty + flame_size), (startx + 8, starty)], 0)

# display final stats when the game is over
def display_final():
    final1 = "Game over"
    final2 = "You landed at %.1f m/s" % velocity
    if velocity > -5:
        final3 = "Nice landing!"
        final4 = "I hear NASA is hiring!"
    elif velocity > -15:
        final3 = "Ouch!  A bit rough, but you survived."
        final4 = "You'll do better next time."
    else:
        final3 = "Yikes!  You crashed a 30 Billion dollar ship."
        final4 = "How are you getting home?"

    pygame.draw.rect(screen, BLACK, (5, 5, 350, 280), 0)
    draw_font(final1, 70, WHITE, (20, 50))
    draw_font(final2, 40, WHITE, (20, 110))
    draw_font(final3, 26, WHITE, (20, 150))
    draw_font(final4, 26, WHITE, (20, 180))

    pygame.display.flip()


myThrottle = ThrottleClass((15, 500))


# calcualte position, motion, acceleration, fuel
def calculate_velocity():
    global thrust, fuel, velocity, delta_v, height, y_pos
    delta_t = 1/FPS
    thrust = (500 - myThrottle.rect.centery) * 5.0  # turn throttle position
                                                    # into amount of thrust
    fuel -= thrust /(10 * FPS)                      # use up fuel
    if fuel < 0:
        fuel = 0.0
    if fuel < 0.1:
        thrust = 0.0
    delta_v = delta_t * (-gravity + 200 * thrust / (ship_mass + fuel))
    velocity += delta_v
    delta_h = velocity * delta_t
    height += delta_h
    y_pos = ground - (height * (ground - start) / 2000) - 90


# main loop
RUNNING = True
while RUNNING:
    clock.tick(FPS)
    FPS = clock.get_fps()
    if FPS < 1:
        FPS = 30

    if height > 0.1:
        calculate_velocity()
        screen.fill(BLACK)
        display_stats()

        # draw the fuel bar and an outline around it
        pygame.draw.rect(screen, BLUE, (80, 350, 24, 100), 2)
        fuelbar = 96 * fuel / 5000
        pygame.draw.rect(screen, GREEN, (84, 448-fuelbar, 18, fuelbar), 0)

        # thrust bar and the thrust handle
        pygame.draw.rect(screen, RED, (25, 300, 10, 200), 0)
        screen.blit(myThrottle.image, myThrottle.rect)
        # place the moon image
        screen.blit(moon, (0, 500, 400, 100))
        # draw the landing pad
        pygame.draw.rect(screen, DARK_GREY, (220, 535, 70, 5),0)

        display_flames()

        screen.blit(ship, (230, y_pos, 50, 90))

        instruct1 = "Land softly without running out of fuel"
        instruct2 = "Good landing: < 15 m/s    Great landing:  < 5m/s"

        draw_font(instruct1, 24, WHITE, (50, 550))
        draw_font(instruct2, 24, WHITE, (20, 575))

        pygame.display.flip()
    else:
        display_final()

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
