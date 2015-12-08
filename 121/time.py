file = "work.txt"
inFile = open(file,'r')
for i in inFile:
	if(inFile):

		time = i
		hour1 = 3600
		minute1 = 60

		extratime = time % hour1
		time2 = time
		hours = (time2 - extratime) / hour1
		
		newextratime = extratime % minute1
		minutes = (extratime - newextratime) / minute1

		seconds = newextratime
		print(hours,minutes,seconds)