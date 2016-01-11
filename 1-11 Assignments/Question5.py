class String(object):
	
	def getString(self):
		self.string = input ("Input a string: ")
	
	def printString(self):
		list = {}
		newstring = []
		for i in range(0, len(self.string)):
			list[i] = self.string[i]
		
		for l in range(0, len(self.string)):
			if(ord(list[l]) <= 122):
				if(ord(list[l]) >= 97):
					list[l] = chr(ord(list[l]) - 32)
				else:
					list[l] = list[l]
			
			else:
				list[l] = list[l]
		
			newstring.append(list[l])
		
		print("".join(newstring))