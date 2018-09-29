#using random function
import random
while True:
	i=input("enter 'n' to quit\nOR\nEnter any number to get a random number:" )
	if(i=='n'):
		print("Thank you.See you next time!")
		exit()
	else:
		print(random.randint(1,6))