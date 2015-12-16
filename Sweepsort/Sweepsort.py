import VecMath
from VecMath import *

class Rect(object):
	def __init__(self,nx,ny,nh,nw,nn):
		self.x = nx
		self.y = ny
		self.height = nh
		self.width = nw
		self.name = nn
		self.min = {self.x - (self.width / 2), self.y - (self.height / 2)}
		self.max = {self.x + (self.width / 2), self.y + (self.height / 2)}