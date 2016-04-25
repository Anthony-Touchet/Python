import node
from node import *
import pygame
from pygame.locals import *
import random
from random import *
import time

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

player.AStar(screen)	#Algorithim that will change the parents of the nodes

for l in searchspace:	#for each list in the searchspace
	for n in l:			#for each node in the list
		if (n in player.closedNodes) and (n != player.start) and (n != player.goal) and (n.walkable == True):	#if the node is in closed list, not the start, not the goal, and walkable is equal to true
			pygame.draw.rect(screen, [0, 0, 255, 255] ,[(n.x, n.y), (n.width, n.height)])						#Draw that the node in in the closed list. Blue Square
			
		elif (n in player.openNodes) and (n != player.goal) and (n != player.start) and (n.walkable != False):	#if the node is in open list, not the start, not the goal, and walkable is equal to true
			pygame.draw.rect(screen, [0, 255, 50, 255] ,[(n.x, n.y), (n.width, n.height)])						#Draw that the node in in the open list. Green Square
		
for l in searchspace:
	for n in l:
		if n.parent != None:						#If the node has a parent
			player.DrawParent(screen, n, n.parent)	#Draw line to that parent
			

player.DrawPath(screen)		#draw from the goal

finish = False
clock = pygame.time.Clock()
while not finish:	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finish = True
	pygame.display.flip()
	
#http://www.pygame.org/docs/