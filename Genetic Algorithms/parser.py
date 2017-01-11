file = "expressions.txt"
inFile = open(file,'r')
for string in inFile:
	if(inFile):			
		numOfClauses = 0;
		literals = [];
		clauseOpen = 0;
		nots = 0;
		ands = 0;
		ors = 0;
		
		for char in string:
			if char == '!':
				nots += 1;
			
			elif  char == ' ':
				continue;
			
			elif  char == '&':
				ands += 1;
				
			elif  char == '|':
				ors += 1;
				
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
		print("# of NOTs: ", nots);
		print("# of ANDs: ", ands);
		print("# of ORs: ", ors);
		print("Number of literals: ", len(literals));
		print("Number of clauses: ", numOfClauses);
		print("\n");