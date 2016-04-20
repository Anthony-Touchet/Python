import node
from node import *
import pygame
from pygame.locals import *
import random
from random import *
import time

pygame.init()
size = width, height = 425, 425
screen = pygame.display.set_mode(size)
searchspace = []	#Search Space where all the nodes will be
ytrack = 0			#Will help track where on the y we are
nodeHold = []		#Temperary node holder

a = Node(- 10, - 10)	#Base sizing node. will not use for actual game

for r in range(0, 7):	#Create Grid
	nodeHold = []
	for i in range(0, 7):#Create Row
		nodeHold.append(Node(i * (a.width + a.space), ytrack))
	searchspace.append(nodeHold) #Add row
	ytrack += nodeHold[0].height + nodeHold[0].space	
player = Astar(searchspace[2][3], searchspace, searchspace[5][5])	#Player	

for r in searchspace:
	for n in r:	
		rand = randrange(0, 5)
		if(rand % 3 == 0) and (player.curNode != n) and (player.goal != n):
			n.walkable = False 
		n.Draw(screen)
		#self.curNode.G = self.Calculate(self.searspace[i][j], self.curNode)
		

player.curNode.H = player.CalculateH(player.curNode, player.goal)
print player.curNode.H

for r in searchspace:
	for n in r:
		n.Draw(screen)

player.Draw(screen)

#if (player.AStar(screen)):
#	player.DrawPath(screen)
	
#else:
#	pygame.draw.line(screen, [0, 100, 100, 255], (player.start.x, player.start.y),(player.start.x + player.start.width, player.start.y + player.start.height), 5)

finish = False
clock = pygame.time.Clock()
while not finish:	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finish = True
	pygame.display.flip()
	
#http://www.pygame.org/docs/