import classes
from classes import *
import time

file = "expressions.txt"
inFile = open(file,'r')

#for string in inFile:
#	if(inFile):	

print("Enter the number corrisponding to the expression: \n")
lineNumber = 0
expressions = []
for line in inFile:
	print(str(lineNumber) + ". " + line)
	expressions.append(line)
	lineNumber += 1

input = input()
input = int(input)
string = expressions[input]

expression = ""
clauses = []
literals = []
popul = []
inClause = "false";
clausesString = "";
log = ""
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

log += (expression + "\n" + "\n")
##Offspring and Mutation
popul = GenRandomValues(len(literals), 10)  ##Generate popul
num = 0
log +=("Inital population:" + " \n ")
for p in popul:
	num += 1
	log +=("Canidate #" + str(num) + " : " + str(p.value) + " \n ")
log += " \n "
solutionFound = 0;
solution = None
gen = 0
start = time.time()
end = None
while(solutionFound == 0):
	gen += 1
	log +=("\n" + "Gen #" + str(gen) + " \n ")
	for can in popul:
		if can.Evaluation(expression, literals, can) >= 1:
			end = time.time()
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
		newCan.value = newCan.Mutate(18)
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
		log += p.PrintCanidate(expression, p.Evaluation(expression, literals, p))
		if p.Evaluation(expression, literals, p) >= 1:
			end = time.time()
			solution = p
			solutionFound = 1;
			break
print(log)
print("This is the solution: " + solution.value)
print("In Gen: " + str(gen))
print("Solution found in: " + str(round((end - start) * 1000.0, 1)) + " miliseconds.")
