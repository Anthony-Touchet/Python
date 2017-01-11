file = "expressions.txt"
inFile = open(file,'r')

print("| - OR");
print("! - NOT");
print("& - AND");
print("( - Open Clause");
print(") - Close Clause");
print("\n");

for string in inFile:
	if(inFile):			
		numOfClauses = 0;
		literals = [];
		clauseOpen = 0;
		nots = 0;
		ands = 0;
		ors = 0;
		
		for char in string:
			if char == '!':			#Opporators
				nots += 1;
			
			elif  char == '&':
				ands += 1;
				
			elif  char == '|':
				ors += 1;
				
			elif  char == ' ':		#Spaces and endings
				continue;
				
			elif  char == '\n':
				continue;
				
			elif  char == '(':		#Clauses
				clauseOpen = 1;
				
			elif  char == ')' and clauseOpen == 1:
				numOfClauses += 1;
				clauseOpen = 0;
				
			else:						#Literals
				if char in literals:	#Checking to see if literals are already in list.
					continue;
					
				literals.append(char);	#Putting Literals inside list
		
		literals.sort();					#clean up list
		print string ;						#Print info on clause
		print "Literals: ", literals ;
		print "# of NOTs: ", nots ;
		print "# of ANDs: ", ands ;
		print "# of ORs: ", ors ;
		print "Number of literals: ", len(literals) ;
		print "Number of clauses: ", numOfClauses ;
		print "\n" ;