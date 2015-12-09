import VecMath
from VecMath import *

print("Vector3D Math:")
a = Vector3D(0,5,0)
b = Vector3D(10,0,0)
c = Vector3D(0,0,0)
result = Vector3D(0,0,0)
print(" ")

c = a + b
print("Addition: ")
c.stats()
print(" ")

print("Magnitue:",c.Magnitude(),"\n")

print("Subtraction: ")
c = a - b
c.stats()
print(" ")

c = a + b
print("Normalize:")
result = c.Normalize()
result.stats()
print(" ")

print("Dot Product:")
print(a * b)
print(" ")

print("Cross Product:")
result = a.Cross(b)
result.stats()
print(" ")

print("LinearInterpolation:")
result = a.lerp(b,.5)
result.stats()
print(" ")

print("Angle:")
result = a.Angle(b)
print(result)
print(" ")
print(" ")

print("VECTOR2D MATH:")

a = Vector2D(5,5)
b = Vector2D(10,10)
c = a + b
c.stats()
print(" ")

print("Magnitue:",c.Magnitude(),"\n")

print("Subtraction: ")
c = a - b
c.stats()
print(" ")

c = a + b
print("Normalize:")
result = c.Normalize()
result.stats()
print(" ")

print("Dot Product:")
print(a * b)
print(" ")

print("LinearInterpolation:")
result = a.lerp(b,.5)
result.stats()
print(" ")

print("Angle:")
result = a.Angle(b)
print(result)
print(" ")

print("EXTRA:")
degrees = 180
print("Degrees to Radians:")
print(DtoR(degrees))
degrees = DtoR(degrees)
print(" ")

print("Radians to Degrees:")
print(RtoD(degrees))
print(" ")

print("HexColor:")
HexColor("DA3778D5")
print(" ")