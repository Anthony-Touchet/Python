import pygame
from pygame.locals import *

class Node(object):
	def __init__(self, position, wal, par):
		self.color = [255, 255, 255, 255]
		self.height = 20
		self.width = 20
		self.x = position[0]
		self.y = position[1]
		self.walkable = wal
		self.margin = 5
		self.top = (self.y + self.margin) * self.y + self.margin
		self.left = (self.x + self.margin) * self.x + self.margin
		self.parent = par
		self.G = 0
		self.H = 0
		self.F = G + H
		
	def draw(self, screen):
		if self.walkable == True:
			pygame.draw.rect(screen, self.color, [self.x, self.y, self.height, self.width])
		else:
			pygame.draw.rect(screen, [0,0, 255, 255], [self.x, self.y, self.height, self.width])
#null = None