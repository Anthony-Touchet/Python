import math
from math import *
class Vector3D(object):
	def __init__(self,nx,ny,nz):	#initalizing Vector and setting values
		self.x = nx
		self.y = ny
		self.z = nz
		
	def stats(self): #Print
		print(self.x,",",self.y,",",self.z)
		
	def __add__(self, other): #Addition
		result = Vector3D(0,0,0)
		result.x = self.x + other.x		#Adding each variable of the two vectors together and setting them equal to the corrisponding vector of result
		result.y = self.y + other.y
		result.z = self.z + other.z
		return result
		
	def __sub__(self, other): #Subtraction
		result = Vector3D(0,0,0)
		result.x = self.x - other.x		#Subtracting each variable from the corrisponding variable of the other vector and storing it into the variable of result
		result.y = self.y - other.y
		result.z = self.z - other.z
		return result
		
	def Magnitude(self): #Magnitude
		result = Vector3D(0,0,0)
		result.x = self.x ^ 2	#Multipling variable by self 
		result.y = self.y ^ 2
		result.z = self.z ^ 2
		newre = sqrt(result.x + result.y + result.z)	#adding all the variables together and square-rooting the result.
		return newre
		
	def Normalize(self): #Normalize
		result = Vector3D(0,0,0)
		if(self.x >= self.y and self.x >= self.z):		#This is to insure that nothing is above 1
			div = self.x
		elif(self.y >= self.x and self.y >= self.z):
			div = self.y
		else:
			div = self.z
		result.x = self.x / div			#Dividing by the largest number and storing it all into result
		result.y = self.y / div
		result.z = self.z / div
		return result				
		
	def __mul__(self, other): #Dot Product
		x = self.x + other.x	#adding all corrisponding variables and then adding each variable to the next
		y = self.y + other.y
		z = self.z + other.z
		return x + y + z
		
	def Cross(self, other): #Cross Product
		result = Vector3D(0,0,0)
		result.x = (self.y * other.z) - (other.y + self.z)	#Finding the dot product by multipling the other values times the third value the subtract each other
		result.y = (self.z * other.x) - (other.z + self.x)
		result.z = (self.x * other.y) - (other.x + self.y)
		return result
		
	def lerp(self, other, per): #LinearInterpolation
		result = Vector3D(0,0,0)
		result.x = self.x + (per * (other.x - self.x))	#finding a point between two vectors by finding the space between them, multipling by percentage then adding to the starting point
		result.y = self.y + (per * (other.y - self.y))
		result.z = self.z + (per * (other.z - self.z))
		return result
		
	def Angle(self, other): #Angle between two Vector3Ds
		opp = self.Magnitude()					#Finding lengh of opposite
		base = other.Magnitude()				#finning lengh of base
		hyp = sqrt((base * base) + (opp * opp))	#finding hypotonouse based off base and opp
		
		tri = Vector3D(base, opp, hyp)			#stores sides in a vector so it can be normalized
		tri = tri.Normalize()					
		
		angle = acos(base / hyp)				#finding acos
		result = (angle / 3.14) * 180			#Answer is in radians aso changing to degrees
		
		return result
		
class Vector2D(object):
	def __init__(self,nx,ny):	#initalizing Vector and setting values
		self.x = nx
		self.y = ny
		
	def stats(self): #Print
		print(self.x,",",self.y)
		
	def __add__(self, other): #Addition
		result = Vector2D(0,0)
		result.x = self.x + other.x		#Adding each variable of the two vectors together and setting them equal to the corrisponding vector of result
		result.y = self.y + other.y
		return result
		
	def __sub__(self, other): #Subtraction
		result = Vector2D(0,0)
		result.x = self.x - other.x		#Subtracting each variable from the corrisponding variable of the other vector and storing it into the variable of result
		result.y = self.y - other.y
		return result
		
	def Magnitude(self): #Magnitude
		result = Vector2D(0,0)
		result.x = self.x ^ 2		#Multipling variable by self 
		result.y = self.y ^ 2
		newre = sqrt(result.x + result.y)	#adding all the variables together and square-rooting the result.
		return newre
		
	def Normalize(self): #Normalize
		result = Vector2D(0,0)
		if(self.x >= self.y):		#This is to insure that nothing is above 1
			div = self.x
		else:
			div = self.y
		result.x = self.x / div		#Dividing by the largest number and storing it all into result
		result.y = self.y / div
		return result
		
	def __mul__(self, other): #Dot Product
		x = self.x + other.x		#adding all corrisponding variables and then adding each variable to the next
		y = self.y + other.y
		return x + y
		
	def lerp(self, other, per): #LinearInterpolation
		result = Vector2D(0,0)
		result.x = self.x + (per * (other.x - self.x))		#Finding the dot product by multipling the other values times the third value the subtract each other
		result.y = self.y + (per * (other.y - self.y))
		return result
		
	def Angle(self, other): #Angle between two Vector3Ds
		opp = self.Magnitude()					#Finding lengh of opposite
		base = other.Magnitude()				#finning lengh of base
		hyp = sqrt((base * base) + (opp * opp))	#finding hypotonouse based off base and opp
		
		tri = Vector3D(base, opp, hyp)			#stores sides in a vector so it can be normalized
		tri = tri.Normalize()					
		
		angle = acos(base / hyp)				#finding acos
		result = (angle / 3.14) * 180			#Answer is in radians aso changing to degrees
		
		return result
	
def DtoR(object): #degrees to radians
		return (object / 180) * 3.14
	
def RtoD(object): #Radians to degrees
	return (object / 3.14) * 180		
		
def HexColor(object): #Hex Color
	red = int(object[:2], 16)		#takes first two characters and converts those two into a hex color in base 10
	green = int(object[2:4], 16)	#takes characters 3 and 4 and converts those two into a hex color in base 10
	blue = int(object[4:6], 16)		#takes characters 5 and 6 and converts those two into a hex color in base 10
	alpha = int(object[6:], 16)		#takes characters 7 and 8 and converts those two into a hex color in base 10
	print(red,green,blue,alpha)