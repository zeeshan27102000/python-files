#playing rock,paper and scissor game
import random
#giving values to variables to limit the number of games
x=0
y=0
#entering the loop
while True:
	a=["r","p","s"]
	C=random.choice(a)
	print("Lets play rock,paper and scissor!!")
	U=input("Enter rock,paper or scissor:")
	print("Computer puts:",C)
	#giving conditions
	if(U=='r' or U=='p' or U=='s'):
		if(U=='r'and C=='s') or (U=='p' and C=='r') or (U=='s' and C=='p'):
			x=x+1
			print("You won",x,"time!!")
		elif(U==C):
			print("It's a tie!")
		else:
			y=y+1
			print("Computer won",y,"time!!")
	else:
		print("Please give proper input")
		break
	if(x==3 or y==3):
		if(x==3):
			print("congratulations!! You won the game!")
		else:
			print("Unfortunately computer won the game!!","\nBetter luck next time!")
		break


