import classes
from classes import *
import time

file = "expressions.txt"
inFile = open(file,'r')

for string in inFile:
	if(inFile):	
		expression = ""
		clauses = []
		literals = []
		popul = []
		inClause = "false";
		clausesString = "";
		for char in string:			                        #Get The phrase
			if char == '!' and inClause == "true":			#Opporators
				clausesString += '~';
			
			elif  char == '&':
				clausesString += char;
				
			elif  char == '|' and inClause == "true":
				clausesString += char;
				
			elif  char == ' ':		                        #Spaces and endings
				continue;
				
			elif  char == '\n':
				continue;
				
			elif  char == '(' and inClause == "false":		#Clauses
				inClause = "true";
				clausesString += '(';
				
			elif  char == ')' and inClause == "true":
				inClause = "false";	
				clausesString += ')';
				clauses.append(clausesString);
				clausesString = "";

			elif inClause == "true":						#Literals
				clausesString += char;
				if char in literals:
					continue;
				literals.append(char);
        
		for string in clauses:
			expression += string
		
		print(expression + "\n")
		##Offspring and Mutation
		popul = GenRandomValues(len(literals), 16)  ##Generate popul
		solutionFound = 0;
		solution = None
		gen = 0
		while(solutionFound == 0):
			gen += 1
			for can in popul:
				if can.Evaluation(expression, literals, can) >= 1:
					print(can.Evaluation(expression, literals, can))
					solution = can
					solutionFound = 1;
					break
			
			breedableCanidates = []	#populate breeding population
			for can in popul:
				breedableCanidates.append(can)
				
			newPopulation = []
			populationCount = len(breedableCanidates)
			for parent in range(0, 4):
				firstParent = breedableCanidates[parent]
				secondParent = Canidate("")
				active = "true"
				while active == "true":
					secondParent = breedableCanidates[random.randrange(parent, len(breedableCanidates))]
					if secondParent in breedableCanidates:
						active = "false"
				child1 = Canidate(secondParent.FlipFrontOffspring(literals, CanidateToList(secondParent)))
				child2 = Canidate(firstParent.FlipFrontOffspring(literals, CanidateToList(firstParent)))
				
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
			
			finalPopulation = []		#Put Children on finalPopulation and have them compete with their parents
			for newCan in newPopulation:
				newCan.value = newCan.Mutate(25)
				finalPopulation.append(newCan)			
				
			for can in popul:		#Strongest parents and children survive
				if len(finalPopulation) < 10:
					finalPopulation.append(can)
				else:
					for check in finalPopulation:
						if can.Evaluation(expression, literals, can) > check.Evaluation(clauses, literals, check):
							check = can
							
			popul = finalPopulation
			for p in popul:
				p.PrintCanidate(expression, p.Evaluation(expression, literals, p))
		print("This is the solution: " + solution.value)
		print("In Gen: " + str(gen))
