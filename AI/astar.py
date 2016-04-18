import node
from node import *
import pygame
from pygame.locals import *

pygame.init()
size = width, height = 1000, 500
screen = pygame.display.set_mode(size)

a = Node([0, 0], True, None)
a.draw(screen)

for i in range(0, 7):
	nodeHold[i] = NodeNode([30 * i, 0], True, None)

done = True
while done:
	i = 6 +2
	
#http://www.pygame.org/docs/