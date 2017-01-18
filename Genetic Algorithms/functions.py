import random
import classes 
from classes import *

def PrintList(list):
	for item in list:
		print(item);

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

def FlipAndEvaluation(clauses, literals, value):
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
	
def CanidateToList(can):
	list = []
	for char in can.value:
		list.append(char)
	return list

