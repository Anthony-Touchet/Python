import node
from node import *
import pygame
from pygame.locals import *
import random
from random import *
import time

def DrawPath(screen):
	cur = self.goal					#where the function will start drawing
	while(cur.parent != None):		#While the parent of the current node is not empty
		pygame.draw.line(screen, [255, 0, 255, 255], cur.center, cur.parent.center, 5)	#Draw line to that parent
		cur = cur.parent		#Set current node to that parent
		pygame.screen.flip()

pygame.init()
size = width, height = 425, 425									#set size of the screen
screen = pygame.display.set_mode(size)							
searchspace = []	#Search Space where all the nodes will be
ytrack = 0			#Will help track where on the y we are
nodeHold = []		#Temperary node holder

a = Node(- 10, - 10)												#Base sizing node. will not use for actual game

for r in range(0, 7):												#Create Grid
	nodeHold = []
	for i in range(0, 7):											#Create Row
		nodeHold.append(Node(i * (a.width + a.space), ytrack))
	searchspace.append(nodeHold) 									#Add row
	ytrack += nodeHold[0].height + nodeHold[0].space	

player = Astar(searchspace[1][1], searchspace, searchspace[5][5])	#Player	

for r in searchspace:				#For each list in the search space
	for n in r:						#For each node in the list
		rand = randrange(0, 5)		#Get Random number
		if(rand % 3 == 0) and (player.curNode != n) and (player.goal != n):		#If Random number is Divisable and the node isn't the player or the goal
			n.walkable = False 			#Set walkable to false
		n.Draw(screen)					#Draw the node to the screen

player.Draw(screen)		#Draw the player and the Goal

finish = False
started = False
path = False
while not finish:	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finish = True
			
	pygame.display.flip()
	time.sleep(.5)
	if started == False:
		player.Start()
		pygame.display.flip()
		started = True
		
	else:	
		player.curNode = player.FindLowestF(player.openNodes)	#Find Node with the Lowest F score
		player.openNodes.remove(player.curNode)				#Remove Current Node from the open list
		player.closedNodes.append(player.curNode)			#Add Current Node to the Closed List
		adj = player.FindSurrounding()				#Find All adjacent Nodes
	
		for n in adj:									#For Each Adjacent Node
			if(n not in player.closedNodes):					#If it is not in the closed list
				if(n not in player.openNodes):					#And not in open list
					if(player.goal in player.openNodes) or (player.curNode == player.goal):				#And if The Goal is in open list or current node is the goal, Break return True.
						path = True
						
					else:											#Else
						n.parent = player.curNode							#Set Parent
						n.SetH(player.CalculateH(n, player.goal))			#Set H
						n.SetG(player.CalculateG(n, player.curNode))		#Set G
						player.openNodes.append(n)						#Put on open list
						
				else:					#Else if the Node is on the open list
					movecost = player.curNode.G + player.CalculateG(player.curNode, n)	#Calculate the G from current node to the other node
					if(movecost < n.G):				#if that cost is less than the current 
						n.parent = player.curNode		#Set parent
						n.SetG(player.CalculateG(player.curNode, n)) 	#CalculateG
						player.openNodes.sort(key = lambda x : x.f)	#Sort the list

	for l in player.searspace:
		for n in l:
			if (n in player.closedNodes) and (n != player.start) and (n != player.goal):
				pygame.draw.rect(screen, [0,0,255,255], [n.x,n.y, n.width, n.height], )
				
			elif (n in player.openNodes) and (n != player.start) and (n != player.goal):
				pygame.draw.rect(screen, [0, 255, 0, 255], [n.x,n.y, n.width, n.height], )
				
			if n.parent != None:
				pygame.draw.line(screen, [255, 0, 0, 255], n.center, n.parent.center, 5)
				pygame.draw.circle(screen, [255, 0, 0, 255], n.center, 10)
	
	
	pygame.display.flip()
	if path == True:
		time.sleep(5)
#http://www.pygame.org/docs/