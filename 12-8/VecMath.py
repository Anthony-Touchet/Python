import math
from math import *
class Vector3D(object):
	def __init__(self,nx,ny,nz):
		self.x = nx
		self.y = ny
		self.z = nz
		
	def stats(self): #Print
		print(self.x,",",self.y,",",self.z)
		
	def __add__(self, other): #Addition
		result = Vector3D(0,0,0)
		result.x = self.x + other.x
		result.y = self.y + other.y
		result.z = self.z + other.z
		return result
		
	def __sub__(self, other): #Subtraction
		result = Vector3D(0,0,0)
		result.x = self.x - other.x
		result.y = self.y - other.y
		result.z = self.z - other.z
		return result
		
	def Magnitude(self): #Magnitude
		result = Vector3D(0,0,0)
		result.x = self.x ^ 2
		result.y = self.y ^ 2
		result.z = self.z ^ 2
		newre = sqrt(result.x + result.y + result.z)
		return newre
		
	def Normalize(self): #Normalize
		result = Vector3D(0,0,0)
		if(self.x >= self.y and self.x >= self.z):
			div = self.x
		elif(self.y >= self.x and self.y >= self.z):
			div = self.y
		else:
			div = self.z
		result.x = self.x / div
		result.y = self.y / div
		result.z = self.z / div
		return result
		
	def __mul__(self, other): #Dot Product
		x = self.x + other.x
		y = self.y + other.y
		z = self.z + other.z
		return x + y + z
		
	def Cross(self, other): #Cross Product
		result = Vector3D(0,0,0)
		result.x = (self.y * other.z) - (other.y + self.z)
		result.y = (self.z * other.x) - (other.z + self.x)
		result.z = (self.x * other.y) - (other.x + self.y)
		return result
		
	def lerp(self, other, per): #LinearInterpolation
		result = Vector3D(0,0,0)
		result.x = self.x + (per * (other.x - self.x))
		result.y = self.y + (per * (other.y - self.y))
		result.z = self.z + (per * (other.z - self.z))
		return result
		
	def Angle(self, other): #Angle between two Vector3Ds
		opp = self.Magnitude()
		base = other.Magnitude()
		hyp = sqrt((base * base) + (opp * opp))
		
		tri = Vector3D(base, opp, hyp)
		tri = tri.Normalize()
		
		angle = acos(base / hyp)
		result = (angle / 3.14) * 180
		
		return result
		
class Vector2D(object):
	def __init__(self,nx,ny):
		self.x = nx
		self.y = ny
		
	def stats(self): #Print
		print(self.x,",",self.y)
		
	def __add__(self, other): #Addition
		result = Vector2D(0,0)
		result.x = self.x + other.x
		result.y = self.y + other.y
		return result
		
	def __sub__(self, other): #Subtraction
		result = Vector2D(0,0)
		result.x = self.x - other.x
		result.y = self.y - other.y
		return result
		
	def Magnitude(self): #Magnitude
		result = Vector2D(0,0)
		result.x = self.x ^ 2
		result.y = self.y ^ 2
		newre = sqrt(result.x + result.y)
		return newre
		
	def Normalize(self): #Normalize
		result = Vector2D(0,0)
		if(self.x >= self.y):
			div = self.x
		else:
			div = self.y
		result.x = self.x / div
		result.y = self.y / div
		return result
		
	def __mul__(self, other): #Dot Product
		x = self.x + other.x
		y = self.y + other.y
		return x + y
		
	def lerp(self, other, per): #LinearInterpolation
		result = Vector2D(0,0)
		result.x = self.x + (per * (other.x - self.x))
		result.y = self.y + (per * (other.y - self.y))
		return result
		
	def Angle(self, other): #Angle between two Vector3Ds
		opp = self.Magnitude()
		base = other.Magnitude()
		hyp = sqrt((base * base) + (opp * opp))
		
		tri = Vector3D(base, opp, hyp)
		tri = tri.Normalize()
		
		angle = acos(base / hyp)
		result = (angle / 3.14) * 180
		
		return result
	
def DtoR(object): #degrees to radians
		return (object / 180) * 3.14
	
def RtoD(object): #Radians to degrees
	return (object / 3.14) * 180		
		
def HexColor(object): #Hex Color
	red = int(object[:2], 16)
	green = int(object[2:4], 16)
	blue = int(object[4:6], 16)
	alpha = int(object[6:], 16)
	print(red,green,blue,alpha)