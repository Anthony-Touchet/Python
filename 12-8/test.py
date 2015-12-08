import VecMath
from VecMath import *

a = Vector(1,2,60)
b = Vector(5,2,96)
c = Vector(0,0,0)
result = Vector(0,0,0)
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