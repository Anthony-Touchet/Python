import pygame
from pygame.locals import *
import time

class Node(object):							#Nodes for visual representation			
	def __init__(self, x, y):
		self.color = [255, 255, 255, 255]	#base color for nodes
		self.height = 50					#Height of the node
		self.width = 50						#Node width
		self.space = 10						#Space between the nodes
		self.x = x							#X position on the screen
		self.y = y							#Y position on the screen
		self.center = (self.x + (self.width / 2), self.y + (self.height / 2))	#Center of the Node
		self.walkable = True				#Can the node be traveled on
		self.parent = None					#Pointing tho the parent of the node
		self.G = None						#The G score of the node
		self.H = 0							#The H score of the Node
		self.F = None						#The F score. Will be G + H
		
	def Draw(self, screen):		#Drawing the node to the screen
		col = self.color if (self.walkable) else (255,0,0)
		pygame.draw.rect(screen, col ,[(self.x, self.y), (self.width, self.height)])

	def SetG(self, value):	#Get the G score update the F score
		self.G = value
		self.F = self.GetF()
		return self.G
	
	def SetH(self, value):	#Get the H score update the F score
		self.H = value
		self.F = self.GetF()
		return self.H
	
	def GetF(self):			#Set the F score for the node
		if self.G == None:
			self.G = 0
		return self.G + self.H
	
	
class Astar(object):				#Class for the Algorithm
	def __init__(self, Start, SearchSpace, Goal):
		self.start = Start				#Where the Algorithm will start
		self.curNode = Start			#Set the current node to the starting node
		self.goal = Goal				#The end of the path. Where the algoritm is trying to get to.
		self.searspace = SearchSpace	#The collection of Nodes for the Algorithm.
		self.openNodes = []				#All the nodes the algorithm can go to
		self.closedNodes = []			#All the nodes the algorithm has been to
		
	def Draw(self, screen):		#Draw the goal and thew starting nodes
		pygame.draw.rect(screen, [0, 255, 255, 255] ,[(self.start.x, self.start.y), (self.start.width, self.start.height)])
		pygame.draw.rect(screen, [150, 100, 255, 255] ,[(self.goal.x, self.goal.y), (self.goal.width, self.goal.height)])
		
	def FindSurrounding(self):	#Finds and returns all adjacent nodes
		adjac = []			#List of Adjacent nodes
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if node == self.curNode:
					pos = (j, i)

		for i,nodes in enumerate(self.searspace):	#get all ajacent based on that current node
			if(pos[1] - 1 <= i <= pos[1] + 1):	#if in a list adjacent to the current node's list
				for j,node in enumerate(nodes):
					if (pos[0] - 1 <= j <= pos[0] + 1) and (self.searspace[i][j].walkable == True) and (self.searspace[i][j] != self.curNode):	#if adjacent, walkable, and not the current Node.
						adjac.append(self.searspace[i][j])		#Put on the Adjacent list
						
		return adjac	#return Adjacents
		
	def CalculateH(self, n1, n2):	#Used to calculate H
		cost = 0
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if self.searspace[i][j] == n1:
					n1pos = [i, j]		#Get n1's position
					
				if(self.searspace[i][j] == n2):
					n2pos = [i, j]		#Get n2's position

		dist = [abs(n1pos[0] - n2pos[0]), abs(n1pos[1] - n2pos[1])]	#calculate distance
		
		while (dist != [0,0]):	#while this distance is not 0,0
			if dist[0] > 0:	#if greater than 1, add cost, minus 1 on distance
				cost += 10
				dist[0] -= 1
				
			if dist[1] > 0:	#if greater than 1, add cost, minus 1 on distance
				cost += 10
				dist[1] -= 1
				
		return cost	
	
	def CalculateG(self, n1, n2):	#Used to calculate G
		cost = 0
		for i,nodes in enumerate(self.searspace):	#find current
			for j,node in enumerate(nodes):
				if self.searspace[i][j] == n1:
					n1pos = [i, j]		#Get n1's position
					
				if(self.searspace[i][j] == n2):
					n2pos = [i, j]		#Get n2's position

		dist = [abs(n1pos[0] - n2pos[0]), abs(n1pos[1] - n2pos[1])]
		
		if(dist[0] > 0) and (dist[1] > 0):	#if both x and y in distance are 1, cost is 14
			cost = 14
			
		else:			#else cost is ten
			cost = 10
				
		return cost
	
	def FindLowestF(self, nodes):	#Function to find the lowest F in a list
		lowestF = None
		for n in nodes:			#for each node in the list
			if lowestF == None:	#if lowest node is none
				lowestF = n		#lowest node is equal to n
				
			elif(n.GetF() < lowestF.GetF()):	#else if n.F is less than LOwestF.F, change
				lowestF = n
		
		return lowestF
		
	def Start(self):
		self.curNode = self.start				#set current node to the start
		
		self.openNodes.append(self.curNode)		#put on the open list
		ad = self.FindSurrounding()				#Find Surrounding nodes
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
			
			if(self.curNode == self.goal) or (self.goal in self.closedNodes):	#And if The Goal is in open list or current node is the goal, Break return True.
				return True
			
			for n in adj:									#For Each Adjacent Node
				if(n not in self.closedNodes):					#If it is not in the closed list
					if(n not in self.openNodes):					#And not in open list						
						n.parent = self.curNode							#Set Parent
						n.SetH(self.CalculateH(n, self.goal))			#Set H
						n.SetG(self.CalculateG(n, self.curNode))		#Set G
						self.openNodes.append(n)						#Put on open list
						
					else:					#Else if the Node is on the open list
						movecost = self.curNode.G + self.CalculateG(self.curNode, n)	#Calculate the G from current node to the other node
						if(movecost < n.G):								#if that cost is less than the current 
							n.parent = self.curNode						#Set parent
							n.SetG(self.CalculateG(self.curNode, n)) 	#CalculateG
							self.openNodes.sort(key = lambda x : x.f)	#Sort the list
							
			
				
		return False	#if the open list is empty, return false

	def DrawParent(self, screen, n1, n2):									#Draw from n1's center to n2's center
		pygame.draw.circle(screen, [255, 0, 0, 255], n1.center, 10)
		pygame.draw.line(screen, [255, 0, 0, 255], n1.center, n2.center, 5)
	
	def DrawPath(self, screen):
		cur = self.goal					#where the function will start drawing
		while(cur.parent != None):		#While the parent of the current node is not empty
			pygame.draw.line(screen, [100, 100, 100, 255], cur.center, cur.parent.center, 5)	#Draw line to that parent
			cur = cur.parent		#Set current node to that parent