import math
from math import *
class Vector(object):
	def __init__(self,nx,ny,nz):
		self.x = nx
		self.y = ny
		self.z = nz
		
	def stats(self): #Print
		print(self.x,",",self.y,",",self.z)
		
	def __add__(self, other): #Addition
		result = Vector(0,0,0)
		result.x = self.x + other.x
		result.y = self.y + other.y
		result.z = self.z + other.z
		return result
		
	def __sub__(self, other): #Subtraction
		result = Vector(0,0,0)
		result.x = self.x - other.x
		result.y = self.y - other.y
		result.z = self.z - other.z
		return result
		
	def Magnitude(self): #Magnitude
		result = Vector(0,0,0)
		result.x = self.x ^ 2
		result.y = self.y ^ 2
		result.z = self.z ^ 2
		newre = sqrt(result.x + result.y + result.z)
		return newre
		
	def Normalize(self): #Normalize
		result = Vector(0,0,0)
		result.x = self.x / self.z
		result.y = self.y / self.z
		result.z = self.z / self.z
		return result
		
	def __mul__(self, other): #Dot Product
		x = self.x + other.x
		y = self.y + other.y
		z = self.z + other.z
		return x + y + z
		
	def Cross(self, other): #Cross Product
		result = Vector(0,0,0)
		result.x = (self.y * other.z) - (other.y + self.z)
		result.y = (self.z * other.x) - (other.z + self.x)
		result.z = (self.x * other.y) - (other.x + self.y)
		return result
		
	def lerp(self, other, per):
		result = Vector(0,0,0)
		result.x = self.x + (per * (other.x - self.x))
		result.y = self.y + (per * (other.y - self.y))
		result.z = self.z + (per * (other.z - self.z))
		return result
		
	
def DtoR(object):
		return (object / 180) * 3.14
	
def RtoD(object):
	return (object / 3.14) * 180		
		
def HexColor(object):
	red = int(object[:2], 16)
	green = int(object[2:4], 16)
	blue = int(object[4:6], 16)
	alpha = int(object[6:], 16)
	print(red,green,blue,alpha)