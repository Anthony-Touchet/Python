import pygame
from pygame.locals import *

class Node(object):
	def __init__(self, x, y):
		self.color = [255, 255, 255, 255]
		self.height = 20
		self.width = 20
		self.space = 5
		self.x = x
		self.y = y
		self.walkable = True
		self.parent = None
		self.G = None
		self.H = None
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
	def __init__(self, curN, SearchSpace, Goal):
		self.curNode = curN
		self.goal = Goal
		self.searspace = SearchSpace
		self.openNodes = []
		self.closedNodes = []
		
	def Draw(self, screen):
		pygame.draw.rect(screen, [0, 255, 0, 255] ,[(self.curNode.x, self.curNode.y), (self.curNode.width, self.curNode.height)])
		pygame.draw.rect(screen, [0, 0, 255, 255] ,[(self.goal.x, self.goal.y), (self.goal.width, self.goal.height)])
		
	def LeastF(self, Nodes):
		lowf = 0
		lowestfNode = None
		for n in Nodes:
			if(lowestfNode == None):
				lowf = n.F
				lowestfNode = node

			if (n.F < lowf):
				lowf = n.F
				lowestfNode = node
		return lowestfNode
	
	def FindSurrounding(self, screen):	
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if node == self.curNode:
					pos = (i, j)
					
					
		for i,nodes in enumerate(self.searspace):	#get all ajacent
			if(pos[0] - 1 <= i <= pos[0] + 1) and (i != None):
				for j,node in enumerate(nodes):
					if (pos[1] - 1 <= j <= pos[1] + 1) and (j != None) and (self.searspace[i][j].walkable == True):						
						self.searspace[i][j].parent = self.curNode
						self.searspace[i][j].SetG(10) if((pos[0] == j) or (pos[1] == i)) else(self.searspace[i][j].SetG(14))
						self.openNodes.append(self.searspace[i][j])
						
		self.openNodes.remove(self.curNode)
		
		for n in self.openNodes:
			pygame.draw.rect(screen, [255, 255, 0, 255] ,[(n.x, n.y), (n.width, n.height)])
		
	
	def RunTime(self):
		self.FindSurrounding()
		for n in self.openNodes:
			print n.G
		