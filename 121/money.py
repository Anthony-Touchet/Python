# file = "work.txt"
# inFile = open(file,'r')
# for i in inFile:
	# if(inFile):

money = 9543
quarter = 25
dime = 10
nickle =5

extramoney = money % quarter
money2 = money - extramoney
quarters = money2 / quarter

extramoney2 = extramoney % dime
money3 = extramoney - extramoney2
dimes = money3 / dime

extramoney3 = extramoney2 % nickle
money4 = extramoney2 - extramoney3
nickles = money4 / nickle

pennies = extramoney3

print("Quarters:",quarters,"\n","Dimes:",dimes,"\n","Nickles:",nickles,"\n","Pennies:",pennies)