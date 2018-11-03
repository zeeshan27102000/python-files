#plotting graph using csv file
import matplotlib.pyplot as grph
#importing csv file
import csv
x=[]
y=[]
with open('square.csv','r') as csvfile:
	plots=csv.reader(csvfile,delimiter=',')
	for row in plots:
		x.append(int(row[0]))
		y.append(int(row[1]))
grph.plot(x,y,marker='*')
grph.title("SQUARES OF NUMBERS")
grph.xlabel("Numbers")
grph.ylabel("Squares")
grph.show()