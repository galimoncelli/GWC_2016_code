import pygame

pygame.init()
screen_width = 700
screen_height = 500
screen = pygame.display.set_mode([screen_width, screen_height])

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