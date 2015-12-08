file = "work.txt"
inFile = open(file,'r')
for i in sorted(inFile):
	if(inFile):
		namelen = len(i)
		if i[namelen - 1] != '\n':
			print (i[:namelen])
			
		else:
			print (i[:namelen - 1])