import functions
from functions import *

file = "expressions.txt"
inFile = open(file,'r')

for string in inFile:
	if(inFile):			
		clauses = []
		literals = []
		popul = []
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
                
		popul = GenRandomValues(len(clauses))  ##Generate popul
		parentSetStrong = []
		parentSetWeak = []
		
		for value in popul:	#Finding the strongest pair
			fitnessRatio = FlipAndEvaluation(clauses, literals, value)
			if len(parentSetStrong) < 2:
				parentSetStrong.append(value)
				
			else:
				for parent in parentSetStrong:	
					if fitnessRatio > value.FlipAndEvaluation(clauses, literals, parent):
						parent = value
						break
		for value in popul:
			if value not in parentSetStrong:
				parentSetWeak.append(value)
		
		##Offspring and Mutation
		strongOffspring1 = CanidateToList(parentSetStrong[1])
		strongOffspring2 = CanidateToList(parentSetStrong[0])
		weakOffspring1 = CanidateToList(parentSetWeak[1])
		weakOffspring2 = CanidateToList(parentSetWeak[0])
			
