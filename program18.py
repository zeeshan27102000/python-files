#rolling of dice
#importing random function
import random
#giving condition
while True:
	i=input("Press 'r' to roll dice and 'q' to quit:")
	if(i=='r'):
		print("You got:",random.randint(1,6))
	if(i=='q'):
		print("Thank you.See you next time!")
		exit()
	
