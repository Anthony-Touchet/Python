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
		pygame.draw.rect(screen, [100, 200, 0, 255] ,[(self.curNode.x, self.curNode.y), (self.curNode.width, self.curNode.height)])
		pygame.draw.rect(screen, [0, 0, 255, 255] ,[(self.goal.x, self.goal.y), (self.goal.width, self.goal.height)])
		
	def LowestF(self, Nodes):
		lowestfNode = None
		
		for n in Nodes:
			if(lowestfNode == None):
				lowestfNode = n

			elif (n.GetF() < lowestfNode.GetF()):
				lowestfNode = n
				
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if node == lowestfNode:
					pos = (j, i)
					
		
		self.openNodes.sort()
		return lowestfNode
	
	def Calculate(self, Node, Node2):						#Trying to calculate H
		for i,nodes in enumerate(self.searspace):	#find Checking node
			for j,node in enumerate(nodes):
				if node == Node:
					Checkpos = (j, i)
		for i,nodes in enumerate(self.searspace):	#find Goal node
			for j,node in enumerate(nodes):
				if node == Node2:
					Goalpos = (j, i)
					Goalpos = (j, i)
			
		cost = 0
		dist = []
		dist.append(abs(Goalpos[0] - Checkpos[0])) 
		dist.append(abs(Goalpos[1] - Checkpos[1]))
		
		for x in range(0, 50):
			if(dist[0] > 0) and (dist[1] > 0):
				cost += 14
				dist[0] = dist[0] - 1
				dist[1] = dist[1] - 1
				
			elif(dist[0] > 0) and (dist[1] <= 0):
				cost += 10
				dist[0] -= 1
				
			elif(dist[0] <= 0) and (dist[1] > 0):
				cost += 10
				dist[1] -= 1
				
			elif(dist[0] <= 0 and dist[1] <= 0):
				break
		return cost
		
	def FindSurrounding(self):	
		self.AdjacentNodes = []
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if node == self.curNode:
					pos = (j, i)

		for i,nodes in enumerate(self.searspace):	#get all ajacent
			if(pos[1] - 1 <= i <= pos[1] + 1) and (i != None):
				for j,node in enumerate(nodes):
					if (pos[0] - 1 <= j <= pos[0] + 1) and (j != None) and (self.searspace[i][j].walkable == True) and (self.searspace[i][j] not in self.closedNodes):						
						self.openNodes.append(self.searspace[i][j])
						self.searspace[j][i].parent = self.curNode
							
	#def ReTracePath(self):
	
	def Run(self):
		self.openNodes.append(self.start)
		while not self.openNodes:
			self.curNode = self.LowestF(self.openNodes)
	
	def AStar(self):
		self.openNodes.append(self.start)
		
		
		while(len(self.openNodes) != 0):
			self.curNode = self.LowestF(self.openNodes)
			self.FindSurrounding()
			self.openNodes.remove(self.curNode)
			self.closedNodes.append(self.curNode)
			
			for node in self.openNodes:
				if(node.walkable == True) and (node not in self.closedNodes):
					if(node not in openNodes):
						if(node == self.goal):
							#Retrace Path
							return true
						else:
							self.openNodes.append(node)
							node.SetG = Calculate(node, current)
							node.SetH = Calculate(node, self.goal)
							
				else:
					costToMoveTo = self.curNode.G + self.curNode.parent.G
					
					if(costToMoveTo < node.G):
						node.parent = self.curNode
						node.SetG(costToMoveTo)
						self.openNodes.sort(key = lambda openNodes: openNodes.G)