import pygame
from pygame.locals import *

class Node(object):
	def __init__(self, x, y):
		self.color = [255, 255, 255, 255]
		self.height = 50
		self.width = 50
		self.space = 10
		self.x = x
		self.y = y
		self.center = (self.x + (self.width / 2), self.y + (self.height / 2))
		self.walkable = True
		self.parent = None
		self.G = None
		self.H = 0
		self.F = None
		
	def Draw(self, screen):
		col = self.color if (self.walkable) else (255,0,0)
		pygame.draw.rect(screen, col ,[(self.x, self.y), (self.width, self.height)])

	def SetG(self, value):
		self.G = value
	
	def SetH(self, value):
		self.H = value
	
	def GetF(self):
		return self.G + self.H
	#null = None
	
class Astar(object):
	def __init__(self, Start, SearchSpace, Goal):
		self.start = Start
		self.curNode = Start
		self.goal = Goal
		self.searspace = SearchSpace
		self.openNodes = []
		self.closedNodes = []
		
	def Draw(self, screen):
		pygame.draw.rect(screen, [100, 200, 0, 255] ,[(self.start.x, self.start.y), (self.start.width, self.start.height)])
		pygame.draw.rect(screen, [150, 100, 255, 255] ,[(self.goal.x, self.goal.y), (self.goal.width, self.goal.height)])
		
	def FindSurrounding(self, screen):	
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if node == self.curNode:
					pos = (j, i)

		for i,nodes in enumerate(self.searspace):	#get all ajacent
			if(pos[1] - 1 <= i <= pos[1] + 1) and (i != None):
				for j,node in enumerate(nodes):
					if (pos[0] - 1 <= j <= pos[0] + 1) and (j != None) and (self.searspace[i][j].walkable == True) and (self.searspace[i][j] not in self.closedNodes) and (self.searspace[i][j] not in self.openNodes) and (self.searspace[i][j] != self.curNode):						
						self.searspace[i][j].parent = self.curNode
						self.openNodes.append(self.searspace[i][j])
						pygame.draw.rect(screen, [255, 255, 0, 255], [self.searspace[i][j].x, self.searspace[i][j].y, self.searspace[i][j].width, self.searspace[i][j].height])
					
	def CalculateH(self, n1, n2):
		cost = 0
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if self.searspace[i][j] == n1:
					n1pos = [i, j]
					
				if(self.searspace[i][j] == n2):
					n2pos = [i, j]

		dist = [abs(n1pos[0] - n2pos[0]), abs(n1pos[1] - n2pos[1])]
		
		while (dist != [0,0]):
			if dist[0] > 0:
				cost += 10
				dist[0] -= 1
				
			if dist[1] > 0:
				cost += 10
				dist[1] -= 1
				
		return cost
		
	def Start(self, screen):
		self.curNode = self.start
		self.openNodes.append(self.curNode)
		while self.curNode in self.openNodes:
			self.FindSurrounding(screen)
			self.openNodes.remove(self.curNode)
			self.closedNodes.append(self.curNode)
	
	def AStar(self, screen):
		
		self.Start(screen)
		
	
	def DrawPath(self, screen):
		node = self.closedNodes[len(self.closedNodes) - 1]
		while(node != self.start):
			pygame.draw.line(screen, [255, 0, 255, 255], node.center, node.parent.center, 5)
			node = node.parent