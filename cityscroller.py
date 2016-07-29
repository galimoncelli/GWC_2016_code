import pygame
import random
from snow_func import *
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

def random_color():
    return random.choice(colors)

# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

class SnowFlake():
    '''
    This class will be used to create the SnowFlake Objects.
    It takes: 
        size - an integer that tells us how big we want the snowflake
        position - a 2 item list that tells us the coordinates of the snowflake (x,y) 
        wind - a boolean that lets us know if there is any wind or not.  
    '''

    def __init__(self, size, position, wind):
        self.size = size
        self.position = position
        self.wind = wind
    
    def fall(self, speed):
        self.position[1] += speed  #moves snowflake in positive y direction
        if self.wind:              #makes wind move random direction when parameter true
            self.position[0] += random.randint(-speed, speed)
        
    def draw(self):
        pygame.draw.circle(screen, WHITE, self.position, 3)



class Building():
	def __init__(self, x_position, y_position, width, height, color):
		self.x_position = x_position
		self.y_position = y_position
		self.width = width
		self.height = height
		self.color = color

	def draw(self):
		pygame.draw.rect(screen, self.color, [self.x_position, self.y_position, self.width, self.height])

	def move(self):
		self.x_position -= 3

city = []


x = 0
snow_list = []
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #BACKGROUND & SNOW
    SPACE = random.randint(1, 6)
    screen.fill(BLACK)
    
    snowflake = SnowFlake(3, [random.randint(0, 750), 0], True)
    snow_list.append(snowflake)
    for snowflake in snow_list:
        snowflake.draw()
        snowflake.fall(1)

    #for buildings
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    if x % SPACE == 0:
    	height = random.randint(50, 300)
    	building = Building(700 + 50, 500 - height, 50, height, color)
    	city.append(building)


    for building in city:
        building.draw()
        building.move()

    x += 1

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE


