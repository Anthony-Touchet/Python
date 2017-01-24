import random
	
def CanidateToList(can):
	list = []
	for char in can.value:
		list.append(char)
	return list


def FindMyIndex(list, case):
	int = 0
	for item in list:
		if item == case:
			return int;
		else:
			int += 1;

def GenRandomValues(literalsLength, max):
        values = []
        for value in range(0, max):
                tempBitString = Canidate("")
                for bit in range(0, literalsLength):
                        rand = random.randrange(0, 100, 1)
                        if rand < 49:
                                tempBitString.value += '1'
                        else:
                                tempBitString.value += '0'
                values.append(tempBitString)
        return values

class Canidate(object):
	def __init__(self, string):
		bitstring = ""
		for bit in string:
			bitstring += bit
		self.value = bitstring
		self.age = 0
		
	def FlipFrontOffspring(self, literals, value):
		for bit in range(len(literals) / 2, len(literals)):
			if value[bit] == '0':
				value[bit - (len(literals) / 2)] = '1'
			elif value[bit] == '1':
				value[bit - (len(literals) / 2)] = '0'
		return value
	
	def Evaluation(self, expression, literals, can):
		tempstring = ""
		clauses = []
		chromoeval = 0
		for string in expression:		                #Switch values
			for char in string:
				if char == ')':
					tempstring += char
					clauses.append(tempstring)
					tempstring = ""
				
				elif char == '&':
					continue
				
				else:
					if char != '~' and char != '(' and char != '|' and char != '&':
						tempstring += can.value[FindMyIndex(literals, char)]
					
					else:
						tempstring += char
						
		finalString = ""
		flip = 0
		for string in clauses:
			for char in string:
				if flip == 1:
					if char == '1':
						finalString += '0'
						
					elif char == '0':
						finalString += '1'
					flip = 0
				else:
					if char == '~':
						flip = 1
					else:
						finalString += char
			clauses[FindMyIndex(clauses, string)] = finalString
			finalString = ""
			
		for c in clauses:
			chromoeval += eval(c)

		return chromoeval / float(len(clauses))

	def Mutate(self, mutationChance):
		finalList = []
		bitString = ""
		for bit in self.value:
			if random.randrange(1, 101, 1) <= mutationChance:
				if bit == '1':
					finalList.append('0')
				elif bit == '0':
					finalList.append('1')
			else:
				finalList.append(bit)
		for bit in finalList:
			bitString += bit
		return bitString
	
	def PrintCanidate(self, expression, fittness):
		log = ""
		log +=("Value: " + self.value + " ")
		log +=("Fittness: " + str(fittness) + " ")
		log += " \n "
		return log
		
	def PercentInheritance(self, percent):	#Percent must be between 0 and 100
		parentValue = self.value
		childValue = ""
		for bit in self.value:
			br = random.randrange(1, 101, 1)
			if br <= percent:
				childValue += bit
			else:
				if bit == '0':
					childValue += '1'
				else:
					childValue += '0'

		return Canidate(childValue)