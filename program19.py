#snake and ladder game
#importing random function
import random
count=0
#giving conditions
while(count<=100):
	n=input("Press 'r' to roll the dice:")
	if(n=='r'):
		r=random.randint(1,6)
		count=count+r
		print("you got:",r)
		print("you move to:",count)
		#giving snake and ladder condition
		if(count==8):
			count=37
			print("you climbed the ladder to:",count)
		elif(count==11):
			count=2
			print("you got snake.You move down to:",count)
		elif(count==13):
			count=34
			print("you climbed the ladder to:",count)
		elif(count==25):
			count=4
			print("you got snake.You move down to:",count)
		elif(count==40):
			count=68
			print("you climbed the ladder to:",count)
		elif(count==52):
			count=81
			print("you climbed the ladder to:",count)
		elif(count==65):
			count=46
			print("you got snake.You move down to:",count)
		elif(count==76):
			count=97
			print("you climbed the ladder to:",count)
		elif(count==89):
			count=70
			print("you got snake.You move down to:",count)
		elif(count==93):
			count=64
			print("you got snake.You move down to:",count)
		elif(count==100):
			print("Congratulations! You won the game!")
			exit()



