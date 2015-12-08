class Vector(x,y,z):
	
	def stats():
		print(x,",",y,",",z)
	
	def VectorCreate(newx, newy, newz):
		x = newx
		y = newy
		z = newz
		
	def plus(self, b):
		newVector = (0,0,0)
		newVector.x = self.x + b.x
		newVector.y = self.y + b.y
		newVector.z = self.z + b.z
		return newVector
	
