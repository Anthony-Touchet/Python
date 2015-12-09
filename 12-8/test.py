import VecMath
from VecMath import *

print("Vector3D Math:")					#3D Vector Math
a = Vector3D(0,5,0)						#Test Vector a
b = Vector3D(10,0,1)					#Test Vector b
c = Vector3D(0,0,0)						#Testing Vector c that will equal the result of anythiny that returns a vector
result = Vector3D(0,0,0)				#If using c, then result will be what is printed
print(" ")

c = a + b								#c = (10, 5, 0)
print("Addition: ")
c.stats()
print(" ")

print("Magnitue:",c.Magnitude(),"\n")	#finding the magnitue of c

print("Subtraction: ")
c = a - b								#Subtraction of two 3D vectors
c.stats()
print(" ")

c = a + b								#Reseting c to something that can more easily be used
print("Normalize:")
result = c.Normalize()					#Normalizing c
result.stats()
print(" ")

print("Dot Product:")					#finding The Dot Product between a and b
print(a * b)
print(" ")

print("Cross Product:")					#finding the cross product between a and b
result = a.Cross(b)
result.stats()
print(" ")

print("LinearInterpolation:")			#finding the vector that is 50 percent between a and b
result = a.lerp(b,.5)
result.stats()
print(" ")

print("Angle:")
result = a.Angle(b)						#Finding the angle between and b
print(result)
print(" ")
print(" ")

print("VECTOR2D MATH:")					#2D Vector Math

a = Vector2D(5,5)						#Redefining Test Vector a
b = Vector2D(10,10)						#Redefining Test Vector b
c = a + b								#Testing Vector c that will equal the result of anythiny that returns a vector
c.stats()								#.stats prints the values of the vector that called it
print(" ")

print("Magnitue:",c.Magnitude(),"\n")	#The Magnitued of c which is a + b

print("Subtraction: ")					#Subtracting 2DVectors
c = a - b
c.stats()
print(" ")

c = a + b								#Setting c back to something more useable
print("Normalize:")
result = c.Normalize()					#Normalizing The c Vector (15,15)
result.stats()
print(" ")

print("Dot Product:")					#Finding the dot product between a and b
print(a * b)
print(" ")

print("LinearInterpolation:")
result = a.lerp(b,.5)					#Finding the vector 50 percent between a and b
result.stats()
print(" ")

print("Angle:")							#Finding the angle between a and b
result = a.Angle(b)
print(result)
print(" ")

print("EXTRA:")							#Functions that do not use vectors in any way
degrees = 180
print("Degrees to Radians:")			
print(DtoR(degrees))					#Degrees to Radians
degrees = DtoR(degrees)
print(" ")

print("Radians to Degrees:")
print(RtoD(degrees))					#Radians To degrees
print(" ")

print("HexColor:")				
HexColor("DA3778D5")					#Converts this string into color: RGBA
print(" ")