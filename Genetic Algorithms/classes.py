import functions
from functions import *

def FindMyIndex(list, case):
	int = 0
	for item in list:
		if item == case:
			return int;
		else:
			int += 1;

class Canidate(object):
	def __init__(self, string):
		self.value = string
		
	def FlipFrontOffspring(self, clauses):
		for bit in range(len(clauses) / 2, len(clauses)):
			if self[bit] == '0':
				self[bit - (len(clauses) / 2)] = '1'
			elif self[bit] == '1':
				self[bit - (len(clauses) / 2)] = '0'
		return self
	
	def FlipAndEvaluation(self, clauses, literals, value):
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