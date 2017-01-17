import functions
from functions import *

file = "expressions.txt"
inFile = open(file,'r')

for string in inFile:
	if(inFile):			
		clauses = []
		literals = []
		values = [0, 1, 0]
		inClause = "false";
		
		clausesString = "";
		for char in string:			                        #Get The phrase
			if char == '!' and inClause == "true":			#Opporators
				clausesString += '~';
			
			elif  char == '&' and inClause == "true":
				clausesString += char;
				
			elif  char == '|' and inClause == "true":
				clausesString += char;
				
			elif  char == ' ':		                        #Spaces and endings
				continue;
				
			elif  char == '\n':
				continue;
				
			elif  char == '(' and inClause == "false":		#Clauses
				inClause = "true";
				
			elif  char == ')' and inClause == "true":
				inClause = "false";	
				clauses.append(clausesString);
				clausesString = "";
			
			elif inClause == "true":						#Literals
				clausesString += char;
				if char in literals:
					continue;
				literals.append(char);
		
		newClauses = []
		tempstring = ""
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
					tempstring += str(values[index])
			
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

			print(eval(finalstring))
			tempstring = ""
			finalstring = ""
