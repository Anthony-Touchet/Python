import pygame
from pygame.locals import *
import time

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
		self.F = self.GetF()
		return self.G
	
	def SetH(self, value):
		self.H = value
		self.F = self.GetF()
		return self.H
	
	def GetF(self):
		if self.G == None:
			self.G = 0
		return self.G + self.H
	
	
class Astar(object):
	def __init__(self, Start, SearchSpace, Goal):
		self.start = Start
		self.curNode = Start
		self.goal = Goal
		self.searspace = SearchSpace
		self.openNodes = []
		self.closedNodes = []
		
	def Draw(self, screen):
		pygame.draw.rect(screen, [0, 255, 255, 255] ,[(self.start.x, self.start.y), (self.start.width, self.start.height)])
		pygame.draw.rect(screen, [150, 100, 255, 255] ,[(self.goal.x, self.goal.y), (self.goal.width, self.goal.height)])
		
	def FindSurrounding(self):	#Finds and returns all adjacent nodes
		adjac = []
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if node == self.curNode:
					pos = (j, i)

		for i,nodes in enumerate(self.searspace):	#get all ajacent
			if(pos[1] - 1 <= i <= pos[1] + 1):
				for j,node in enumerate(nodes):
					if (pos[0] - 1 <= j <= pos[0] + 1) and (self.searspace[i][j].walkable == True) and (self.searspace[i][j] != self.curNode):	
						adjac.append(self.searspace[i][j])
						
		return adjac
		
	def CalculateH(self, n1, n2):	#Used to calculate H
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
	
	def CalculateG(self, n1, n2):	#Used to calculate G
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
	
	def FindLowestF(self, nodes):	#Function to find the lowest F in a list
		lowestF = None
		for n in nodes:
			if lowestF == None:
				lowestF = n
				
			elif(n.GetF() < lowestF.GetF()):
				lowestF = n
		
		return lowestF
		
	def Start(self):
		self.curNode = self.start		#set current node to the start
		
		self.openNodes.append(self.curNode)		#put on the open list
		ad = self.FindSurrounding()		#Find Surrounding nodes
		for n in ad:							#for each node that is adjacent
			if(n.walkable == True):							#If walkable
				n.parent = self.curNode						#Set Parent
				n.SetH(self.CalculateH(n, self.goal))		#Set the H
				n.SetG(self.CalculateG(n, self.curNode))	#Set the G
				self.openNodes.append(n)					#Put on the open list
				
		self.openNodes.remove(self.curNode)		#Remove starting node
		self.closedNodes.append(self.curNode)	#Put Starting node on the closed list
		
	def AStar(self):
		
		self.Start()									#Run the start function	
		while(len(self.openNodes) > 0):						#While there are nodes in the open list
			self.curNode = self.FindLowestF(self.openNodes)	#Find Node with the Lowest F score
			self.openNodes.remove(self.curNode)				#Remove Current Node from the open list
			self.closedNodes.append(self.curNode)			#Add Current Node to the Closed List
			adj = self.FindSurrounding()				#Find All adjacent Nodes
	
			for n in adj:									#For Each Adjacent Node
				if(n not in self.closedNodes):					#If it is not in the closed list
					if(n not in self.openNodes):					#And not in open list						
						n.parent = self.curNode							#Set Parent
						n.SetH(self.CalculateH(n, self.goal))			#Set H
						n.SetG(self.CalculateG(n, self.curNode))		#Set G
						self.openNodes.append(n)						#Put on open list
						
					else:					#Else if the Node is on the open list
						movecost = self.curNode.G + self.CalculateG(self.curNode, n)	#Calculate the G from current node to the other node
						if(movecost < n.G):				#if that cost is less than the current 
							n.parent = self.curNode		#Set parent
							n.SetG(self.CalculateG(self.curNode, n)) 	#CalculateG
							self.openNodes.sort(key = lambda x : x.f)	#Sort the list
							
			if(self.curNode == self.goal) or (self.goal in self.closedNodes):				#And if The Goal is in open list or current node is the goal, Break return True.
				return True
				
		return False	#if the open list is empty, return false

	def DrawParent(self, screen, n1, n2):	#Draw from n1 to n2
		pygame.draw.circle(screen, [255, 0, 0, 255], n1.center, 10)
		pygame.draw.line(screen, [255, 0, 0, 255], n1.center, n2.center, 5)
	
	def DrawPath(self, screen):
		cur = self.goal					#where the function will start drawing
		while(cur.parent != None):		#While the parent of the current node is not empty
			pygame.draw.line(screen, [100, 100, 100, 255], cur.center, cur.parent.center, 5)	#Draw line to that parent
			cur = cur.parent		#Set current node to that parent