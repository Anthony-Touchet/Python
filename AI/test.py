import pygame
from math import pi
from pygame.locals import *

pygame.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

size = width, height = 1000, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
compl = True

while compl:
	clock.tick(60)
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			compl = False
		elif event.type == pygame.MOUSEMOTION:
			pos = pygame.mouse.get_pos()
			pygame.draw.rect(screen, GREEN, [pos[0], pos[1], 10, 10])
			
	pygame.draw.line(screen, GREEN, [0, 0], [50, 30], 5)
	
	pygame.draw.rect(screen, GREEN, [75, 10, 50, 20], 2)
	
	pygame.draw.rect(screen, GREEN, [150, 10, 50, 20])
	
	pygame.display.flip()
	
#http://www.pygame.org/docs/ref/event.html