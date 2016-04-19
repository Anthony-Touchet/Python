import node
from node import *
import pygame
from pygame.locals import *
import random
from random import *

pygame.init()
size = width, height = 250, 250
screen = pygame.display.set_mode(size)
searchspace = []	#Search Space where all the nodes will be
ytrack = 0			#Will help track where on the y we are
nodeHold = []		#Temperary node holder

a = Node(- 10, - 10)	#Base sizing node. will not use for actual game

for r in range(0, 7):	#Set row
	nodeHold = []
	for i in range(0, 7):#Create Row
		nodeHold.append(Node(i * (a.width + a.space), ytrack))

	searchspace.append(nodeHold)
	ytrack += nodeHold[0].height + nodeHold[0].space	

player = Astar(searchspace[3][2], searchspace, searchspace[5][5])
	
for r in searchspace:	# Set if walkable
	for n in r:
		rand = randrange(0, 5)
		if(rand % 3 == 0) and (player.curNode != n) and (player.goal != n):
			n.walkable = False 
		n.Draw(screen)

player.Draw(screen)

player.FindSurrounding(screen)
	

#Keeps screen up for now
finish = False
while not finish:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finish = True
	
	pygame.display.flip()
	
#http://www.pygame.org/docs/