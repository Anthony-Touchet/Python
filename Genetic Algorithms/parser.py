import classes
from classes import *
import random

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
        
		##Offspring and Mutation
		popul = GenRandomValues(len(clauses))  ##Generate popul

		breedableCanidates = []	#populate breeding population
		for can in popul:
			breedableCanidates.append(can)
			
		newPopulation = []
		populationCount = len(breedableCanidates)
		for parent in range(0, populationCount / 2):
			firstParent = breedableCanidates[parent]
			secondParent = Canidate("")
			active = "true"
			while active == "true":
				secondParent = breedableCanidates[random.randrange(parent, len(breedableCanidates))]
				if secondParent in breedableCanidates:
					active = "false"
			child1 = Canidate(secondParent.FlipFrontOffspring(clauses, CanidateToList(secondParent)))
			child2 = Canidate(firstParent.FlipFrontOffspring(clauses, CanidateToList(firstParent)))
			
			newPopulation.append(child1)
			newPopulation.append(child2)
			if firstParent in breedableCanidates:
				breedableCanidates.remove(firstParent)
			if secondParent in breedableCanidates:
				breedableCanidates.remove(secondParent)
				
			for can in newPopulation:
				bitString = ""
				for bit in can.value:
					bitString += bit
				can.value = bitString
		
		for newCan in newPopulation:
			newCan.value = newCan.Mutate(14)
			popul.append(newCan)

		print(len(popul))	
