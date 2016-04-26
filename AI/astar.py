import node
from node import *
import pygame
from pygame.locals import *
import random
from random import *
import time

def Reset(screen, col, row):
	searchspace = []	#Search Space where all the nodes will be
	ytrack = 0			#Will help track where on the y we are
	nodeHold = []		#Temperary node holder

	a = Node(- 10, - 10)												#Base sizing node. will not use for actual game

	for r in range(0, col):												#Create Grid
		nodeHold = []
		for i in range(0, row):											#Create Row
			nodeHold.append(Node(i * (a.width + a.space), ytrack))
		searchspace.append(nodeHold) 									#Add row
		ytrack += nodeHold[0].height + nodeHold[0].space	

	AI = Astar(None, searchspace, None)	#AI	

	for r in searchspace:				#For each list in the search space
		for n in r:						#For each node in the list
			rand = randrange(0, 5)		#Get Random number
			if(rand % 3 == 0) and (AI.curNode != n) and (AI.goal != n):		#If Random number is Divisable and the node isn't the AI or the goal
				n.walkable = False 			#Set walkable to false
			n.Draw(screen)					#Draw the node to the screen
	
	return AI
	
pygame.init()
size = width, height = 600, 600									#set size of the screen
screen = pygame.display.set_mode(size)

player = Reset(screen, 10, 10)

finish = False
started = None
path = False
drawnode = player.goal
while not finish:	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finish = True
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				finish = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			if player.start == None:
				for l in player.searspace:
					for n in l:
						if (n.x <= pos[0] <= n.x + n.width) and (n.y <= pos[1] <= n.y + n.height):
							player.start = n
							pygame.draw.rect(screen, [0, 255, 255, 255] ,[(player.start.x, player.start.y), (player.start.width, player.start.height)])
			else:
				for l in player.searspace:
					for n in l:
						if (n.x <= pos[0] <= n.x + n.width) and (n.y <= pos[1] <= n.y + n.height):
							player.goal = n
							if(player.start != None) and (player.goal != None):
								started = False
								pygame.draw.rect(screen, [150, 100, 255, 255] ,[(player.goal.x, player.goal.y), (player.goal.width, player.goal.height)])
		
	pygame.display.flip()
	if started == False:
		player.Start()
		pygame.display.flip()
		started = True
		
	elif started == True:
		if(len(player.openNodes) > 0):
			player.curNode = player.FindLowestF(player.openNodes)	#Find Node with the Lowest F score
			player.openNodes.remove(player.curNode)				#Remove Current Node from the open list
			player.closedNodes.append(player.curNode)			#Add Current Node to the Closed List
			adj = player.FindSurrounding()				#Find All adjacent Nodes
	
			for n in adj:									#For Each Adjacent Node
				if(n not in player.closedNodes):					#If it is not in the closed list
					if(n not in player.openNodes):					#And not in open list
						if(player.curNode == player.goal) or (player.goal in player.closedNodes):				#And if The Goal is in open list or current node is the goal, Break return True.
							path = True
							player.DrawPath(screen)
						
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
		
		else:
			pygame.draw.line(screen, [255, 0, 255, 255], [0, 0], [width, height], 10)
			pygame.draw.line(screen, [255, 0, 255, 255], [0, height], [width, 0], 10)
			pygame.display.flip()
			time.sleep(3)
			pygame.draw.rect(screen, [0,0,0,255], [0, 0, size[0], size[1]])
			player = Reset(screen, 10, 10)
			finish = False
			started = False
			path = False
			drawnode = player.goal
			started = None
			player.start = None
			player.goal = None
			
		time.sleep(.5)
	if(path == False):
		for l in player.searspace:
			for n in l:
				if (n in player.closedNodes) and (n != player.start) and (n != player.goal) and (path == False):
					pygame.draw.rect(screen, [0,0,255,255], [n.x,n.y, n.width, n.height], )
				
				elif (n in player.openNodes) and (n != player.start) and (n != player.goal) and (path == False):
					pygame.draw.rect(screen, [0, 255, 0, 255], [n.x,n.y, n.width, n.height], )
				
				if (n.parent != None) and (path == False):
					pygame.draw.line(screen, [255, 0, 0, 255], n.center, n.parent.center, 5)
					pygame.draw.circle(screen, [255, 0, 0, 255], n.center, 10)
	
	else:
		pygame.display.flip()
		time.sleep(3)
		pygame.draw.rect(screen, [0,0,0,255], [0, 0, size[0], size[1]])
		player = Reset(screen, 10, 10)
		finish = False
		started = False
		path = False
		drawnode = player.goal
		started = None
		player.start = None
		player.goal = None
		
		
	pygame.display.flip()
#http://www.pygame.org/docs/