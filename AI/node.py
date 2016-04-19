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
	def __init__(self, curN, SearchSpace, Goal):
		self.curNode = curN
		self.goal = Goal
		self.searspace = SearchSpace
		self.openNodes = []
		self.closedNodes = []
		
	def Draw(self, screen):
		pygame.draw.rect(screen, [100, 200, 0, 255] ,[(self.curNode.x, self.curNode.y), (self.curNode.width, self.curNode.height)])
		pygame.draw.rect(screen, [0, 0, 255, 255] ,[(self.goal.x, self.goal.y), (self.goal.width, self.goal.height)])
		
	def LowestF(self, Nodes, screen):
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
					pygame.draw.line(screen, [0, 255, 255, 255] ,self.curNode.center, node.center, 5)
		
		for n in Nodes:
			print n.GetF()
		return lowestfNode
	
	def CalculateH(self, Node):
		for i,nodes in enumerate(self.searspace):	#find Checking node
			for j,node in enumerate(nodes):
				if node == Node:
					Checkpos = (j, i)
		for i,nodes in enumerate(self.searspace):	#find Goal node
			for j,node in enumerate(nodes):
				if node == self.goal:
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
		
	def FindSurrounding(self, screen):	
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if node == self.curNode:
					pos = (j, i)
					
					
		for i,nodes in enumerate(self.searspace):	#get all ajacent
			if(pos[1] - 1 <= i <= pos[1] + 1) and (i != None):
				for j,node in enumerate(nodes):
					if (pos[0] - 1 <= j <= pos[0] + 1) and (j != None) and (self.searspace[i][j].walkable == True):						
						self.searspace[i][j].parent = self.curNode
						self.searspace[i][j].SetG(10) if((pos[0] == j) or (pos[1] == i)) else(self.searspace[i][j].SetG(14))
						hcost = self.CalculateH(self.searspace[i][j])
						self.searspace[i][j].SetH(hcost)
						self.openNodes.append(self.searspace[i][j])
						
		self.openNodes.remove(self.curNode)
		self.closedNodes.append(self.curNode)
		
		#for n in self.openNodes:
		#	pygame.draw.rect(screen, [255, 100, 0, 255] ,[(n.x, n.y), (n.width, n.height)])
		
	
	def RunTime(self):
		self.FindSurrounding()
		
		