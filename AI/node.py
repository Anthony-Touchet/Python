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
		adjac = []
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if node == self.curNode:
					pos = (j, i)

		for i,nodes in enumerate(self.searspace):	#get all ajacent
			if(pos[1] - 1 <= i <= pos[1] + 1) and (i != None):
				for j,node in enumerate(nodes):
					if (pos[0] - 1 <= j <= pos[0] + 1) and (j != None) and (self.searspace[i][j].walkable == True) and (self.searspace[i][j] != self.curNode):						
						adjac.append(self.searspace[i][j])
						
		return adjac
		
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
	
	def CalculateG(self, n1, n2):
		cost = 0
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if self.searspace[i][j] == n1:
					n1pos = [i, j]
					
				if(self.searspace[i][j] == n2):
					n2pos = [i, j]

		dist = [abs(n1pos[0] - n2pos[0]), abs(n1pos[1] - n2pos[1])]
		
		if(dist[0] > 0) and (dist[1] > 0):
			cost = 14
			
		else:
			cost = 10
				
		return cost
	
	def FindLowestF(self, nodes):
		lowestF = None
		for n in nodes:
			if lowestF == None:
				lowestF = n
				
			elif(n.F < lowestF.F):
				lowestF = n
		
		return lowestF
		
	def Start(self, screen):
		self.curNode = self.start
		self.curNode.G = 0
		self.curNode.G = self.CalculateH(self.curNode, self.goal)
		
		self.openNodes.append(self.curNode)
		while self.curNode in self.openNodes:
			ad = self.FindSurrounding(screen)
			for n in ad:
				if(n.walkable == True):
					n.parent = self.curNode
					n.H = self.CalculateH(n, self.goal)
					n.G = self.CalculateG(n, self.curNode)
					self.openNodes.append(n)
			self.openNodes.remove(self.curNode)
			self.closedNodes.append(self.curNode)
	
	def AStar(self, screen):
		
		self.Start(screen)
		while(len(self.openNodes) > 0):
			self.curNode = self.FindLowestF(self.openNodes)
			self.openNodes.remove(self.curNode)
			self.closedNodes.append(self.curNode)
			adj = self.FindSurrounding(screen)
			
			for n in adj:
				if(n not in self.closedNodes):
					if(n not in self.openNodes):
						if(self.curNode == self.goal):
							return True
						
						else:
							self.openNodes.append(n)
							
							n.parent = self.curNode
							n.H = self.CalculateH(n, self.goal)
							n.G = self.CalculateG(n, self.curNode)
					
					else:
						movecost = self.curNode.G + self.curNode.parent.G
						if(movecost < n.G):
							n.parent = self.curNode
							n.G = movecost
							self.openNodes.sort(key = lambda x : x.f)
		return False

	def DrawPath(self, screen):
		node = self.goal
		while(node.parent != None):
			pygame.draw.line(screen, [255, 0, 0, 255], node.center, node.parent.center, 5)
			node = node.parent