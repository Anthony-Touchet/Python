file = "expressions.txt"
inFile = open(file,'r')
for string in inFile:
	if(inFile):			
		numOfClauses = 0;
		literals = [];
		clauseOpen = 0;
		
		for char in string:
			if char == '!':
				continue;
			
			elif  char == ' ':
				continue;
			
			elif  char == '&':
				continue;
				
			elif  char == '|':
				continue;
				
			elif  char == '\n':
				continue;
				
			elif  char == '(':
				clauseOpen = 1;
				
			elif  char == ')' and clauseOpen == 1:
				numOfClauses += 1;
				clauseOpen = 0;
				
			else:
				if char in literals:
					continue;
					
				literals.append(char);
		
		literals.sort();
		print(string);
		print("Literals: ", literals);
		print("Number of literals: ", len(literals));
		print("Number of clauses: ", numOfClauses);
		print("\n");