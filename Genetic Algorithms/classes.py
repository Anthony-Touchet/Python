import random

def PrintList(list):
	for item in list:
		print(item);
	
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

def GenRandomValues(clauseLength):
        values = []
        for value in range(0, 4):
                tempBitString = Canidate("")
                for bit in range(0, clauseLength):
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
		
	def FlipFrontOffspring(self, clauses, value):
		for bit in range(len(clauses) / 2, len(clauses)):
			if value[bit] == '0':
				value[bit - (len(clauses) / 2)] = '1'
			elif value[bit] == '1':
				value[bit - (len(clauses) / 2)] = '0'
		return value
	
	def Evaluation(self, clauses, literals, value):
		tempstring = ""
		chromoeval = 0
		for string in clauses:		                #Switch values
			for char in string:
				
				if char == '~':			#Opporators
						tempstring += '~'
				
				elif  char == '&':
						tempstring += '&'
					
				elif  char == '|':
						tempstring += '|'				
				
				else:						#Literals
					index = FindMyIndex(literals, char)
					tempstring += str(value.value[index])
				
			flip = 0
			finalstring = ""
			for char in tempstring:         #Do inverses of 1's and 0's
				if flip == 1:
					if char == '1':
						finalstring += str(0)
						
					elif char == '0':
						finalstring += str(1)
					flip = 0
				
				elif char == '~' and flip == 0: #if Inverse operator
					flip = 1
						
				else:
					finalstring += char

			chromoeval +=(eval(finalstring))
			tempstring = ""
			finalstring = ""
		return chromoeval;

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