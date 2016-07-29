import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (127, 127, 127)

possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE, GREY]

pygame.init()


# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Ball Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


#Bouncing Ball Class Code
class BouncingBall():
    #constructor method
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):
        self.x_location = x_location
        self.y_location = y_location
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.ball_size = ball_size

    #ballmethods
    def flashBounce(self, screen, colors, SCREEN_WIDTH, SCREEN_HEIGHT):
       
       ball_color =  random.choice(possible_ball_colors)
       if self.x_location >= SCREEN_WIDTH - self.ball_size or self.x_location < self.ball_size :
            self.x_speed = self.x_speed * -1

       if self.y_location >= SCREEN_HEIGHT - self.ball_size or self.y_location < self.ball_size :
            self.y_speed = self.y_speed * -1


       self.x_location += self.x_speed
       self.y_location += self.y_speed

       pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)

ball1 = BouncingBall(5, 5, 1, 1, 5)
ball2 = BouncingBall(20, 10, 2, 3, 7)
ball3 = BouncingBall(40, 30, 31, 4, 10)

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # background image.
    screen.fill(GREEN)

    # --- Drawing code should go here
    ball1.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball2.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    ball3.flashBounce(screen, possible_ball_colors, SCREEN_WIDTH, SCREEN_HEIGHT)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
