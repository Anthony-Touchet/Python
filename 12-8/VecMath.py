import math
from math import *
class Vector(object):
	def __init__(self,nx,ny,nz):
		self.x = nx
		self.y = ny
		self.z = nz
		
	def stats(self):
		print(self.x,",",self.y,",",self.z)
		
	def __add__(self, other):
		result = Vector(0,0,0)
		result.x = self.x + other.x
		result.y = self.y + other.y
		result.z = self.z + other.z
		return result
		
	def __sub__(self, other):
		result = Vector(0,0,0)
		result.x = self.x - other.x
		result.y = self.y - other.y
		result.z = self.z - other.z
		return result
		
	def Magnitude(self):
		result = Vector(0,0,0)
		result.x = self.x ^ 2
		result.y = self.y ^ 2
		result.z = self.z ^ 2
		newre = sqrt(result.x + result.y + result.z)
		return newre