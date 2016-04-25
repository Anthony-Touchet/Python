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
player = Astar(searchspace[1][1], searchspace, searchspace[5][5])	#Player	

for r in searchspace:
	for n in r:	
		rand = randrange(0, 5)
		if(rand % 3 == 0) and (player.curNode != n) and (player.goal != n):
			n.walkable = False 
		n.Draw(screen)
		
for r in searchspace:
	for n in r:
		n.Draw(screen)

player.Draw(screen)

player.AStar(screen)

for l in searchspace:
	for n in l:
		if (n in player.closedNodes) and (n != player.start) and (n != player.goal) and (n.walkable != False):
			pygame.draw.rect(screen, [0, 0, 255, 255] ,[(n.x, n.y), (n.width, n.height)])
			
		elif (n in player.openNodes) and (n != player.goal) and (n != player.start) and (n.walkable != False):
			pygame.draw.rect(screen, [0, 255, 50, 255] ,[(n.x, n.y), (n.width, n.height)])
		
		if n.parent != None:
			player.DrawParent(screen, n, n.parent)
			

player.DrawPath(screen)

finish = False
clock = pygame.time.Clock()
while not finish:	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finish = True
	pygame.display.flip()
	
#http://www.pygame.org/docs/