#identifying the grades 
a=int(input("what are your marks?:"))
if(a>=90):
	print("your grade is A+")
elif(a>=80):
	print("your grade is A")
elif(a>=70):
	print("your grade is B+")
elif(a>=60):
	print("your grade is B")
elif(a>=50):
	print("you have passed the exam")
else:
	print("you have failed")