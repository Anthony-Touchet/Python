def FindMyIndex(list, case):
	int = 0
	for item in list:
		if item == case:
			return int;
		else:
			int += 1;

def PrintList(list):
	for item in list:
		print(item)