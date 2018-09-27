#mathematical operations using functions and if conditions
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
c=input("which mathematical operation do you want perform +,-,x or /?")
#defining add()
def add():
	print("Addition of two numbers is:",a+b)
	return
#defining sub()
def sub():
	print("subtraction of two numbers is:",a-b)
	return
#defining mul()
def mul():
	print("multipication of two numbers is:",a*b)
	return
#defining div()
def div():
	print("division of two numbers is:",a/b)
	return
#giving conditions
if(c=='+'):
	add()
elif(c=='-'):
	sub()
elif(c=='x'):
	mul()
elif(c=='/'):
	div()
else:
	print("Please give proper input")
