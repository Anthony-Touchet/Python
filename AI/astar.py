import node
from node import *
import pygame
from pygame.locals import *
import random
from random import *
import time
	
searchspace = []	#Search Space where all the nodes will be
ytrack = 0			#Will help track where on the y we are
nodeHold = []		#Temperary node holder	
a = Node(- 10, - 10)

pygame.init()
size = width, height = 600, 600									#set size of the screen
screen = pygame.display.set_mode(size)

for r in range(0, 10):												#Create Grid
	nodeHold = []
	for i in range(0, 10):											#Create Row
		nodeHold.append(Node(i * (a.width + a.space), ytrack))
	searchspace.append(nodeHold) 									#Add row
	ytrack += nodeHold[0].height + nodeHold[0].space	

AI = Astar(searchspace[1][1], searchspace, searchspace[8][8])			#AI	

for r in searchspace:													#For each list in the search space
	for n in r:															#For each node in the list
		rand = randrange(0, 5)											#Get Random number
		if(rand % 3 == 0) and (AI.curNode != n) and (AI.goal != n):		#If Random number is Divisable and the node isn't the AI or the goal
			n.walkable = False 											#Set walkable to false
		n.Draw(screen)	

AI.Draw(screen)

if(AI.AStar()):						#if AStar finds the goal
		for n in AI.openNodes:		#for each node in open list and if the node isn't the goal
			if n != AI.goal:	
				pygame.draw.rect(screen, [0, 255, 0, 255] ,[(n.x, n.y), (n.width, n.height)])	#mark it
		for n in AI.closedNodes:																#for each node in the closed list
			if(n != AI.start) and (n != AI.goal):												#If the node isn't the player or goal
				pygame.draw.rect(screen, [0, 0, 255, 255] ,[(n.x, n.y), (n.width, n.height)])	#Mark it
				
		for l in AI.searspace:																	#for each list in the space
			for n in l:																			#For each node in the list
				if n.parent != None:															#if the node has a parent, draw to the parent
					pygame.draw.line(screen, [255, 0, 0, 255], n.center, n.parent.center, 5)
					pygame.draw.circle(screen, [255, 0, 0, 255], n.center, 10, 0)
		AI.DrawPath(screen)																		#Draw path from the goal to the start
else:								#If AStar return's false
	for n in AI.openNodes:		#for each node in open list and if the node isn't the goal
			if n != AI.goal:	
				pygame.draw.rect(screen, [0, 255, 0, 255] ,[(n.x, n.y), (n.width, n.height)])	#mark it
	for n in AI.closedNodes:																	#for each node in the closed list
		if(n != AI.start) and (n != AI.goal):													#If the node isn't the player or goal
			pygame.draw.rect(screen, [0, 0, 255, 255] ,[(n.x, n.y), (n.width, n.height)])		#Mark it
				
	for l in AI.searspace:																		#for each list in the space
		for n in l:																				#For each node in the list
			if n.parent != None:																#if the node has a parent, draw to the parent
				pygame.draw.line(screen, [255, 0, 0, 255], n.center, n.parent.center, 5)
				pygame.draw.circle(screen, [255, 0, 0, 255], n.center, 10, 0)
	pygame.draw.line(screen, [100, 100, 100, 255], [0, 0], size, 10)
		
finish = False
started = None
while not finish:								#While not done
	for event in pygame.event.get():			#Search for ending event
		if event.type == pygame.QUIT:
			finish = True
		elif event.type == pygame.KEYDOWN:		#else search for space bar to end program
			if event.key == pygame.K_SPACE:
				finish = True
				
#			elif event.key == K_w:
#				pos = pygame.mouse.get_pos()
#				for l in player.searspace:
#					for n in l:
#						if (n.x <= pos[0] <= n.x + n.width) and (n.y <= pos[1] <= n.y + n.height):
#							n.walkable = True if(n.walkable == False) else	 False
#							n.Draw(screen)
#							
#		elif event.type == pygame.MOUSEBUTTONDOWN:
#			pos = pygame.mouse.get_pos()
#			if player.start == None:
#				for l in player.searspace:
#					for n in l:
#						if (n.x <= pos[0] <= n.x + n.width) and (n.y <= pos[1] <= n.y + n.height):
#							n.walkable = True
#							player.start = n
#							pygame.draw.rect(screen, [0, 255, 255, 255] ,[(player.start.x, player.start.y), (player.start.width, player.start.height)])
#			else:
#				for l in player.searspace:
#					for n in l:
#						if (n.x <= pos[0] <= n.x + n.width) and (n.y <= pos[1] <= n.y + n.height):
#							n.walkable = True
#							player.goal = n
#							if(player.start != None) and (player.goal != None):
#								started = False
#								pygame.draw.rect(screen, [150, 100, 255, 255] ,[(player.goal.x, player.goal.y), (player.goal.width, player.goal.height)])

	pygame.display.flip()