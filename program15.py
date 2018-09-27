#mathematical operations using functions
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
#Defining add()
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
#defining mod()
def mod():
	print("remainder of two numbers is:",a%b)
	return
#defining sqrt()
def sqrt():
	print("sqare root of one number is:",a**2,"\nsquare root of another number is:",b**2)
	return
#defining int()
def intr():
	print("integer part of division of two numbers is:",a//b)
	return
#calling all funtions
add()
sub()
mul()
div()
mod()
sqrt()
intr()