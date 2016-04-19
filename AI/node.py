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
		lowf = -1
		lowestfNode = None
		for n in Nodes:
			if(lowestfNode == None):
				lowf = n.F
				lowestfNode = node

			if (n.F < lowf):
				lowf = n.F
				lowestfNode = node
		return lowestfNode
	
	def FindSurrounding(self):
		pos = x, y = 0, 0
		for r in searspace:
			for n in r:
				if(n == curNode):
					pos.x = n
					pos.y = r
		return pos