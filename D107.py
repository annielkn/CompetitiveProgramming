from math import sqrt
def triangular(y):
	z = 8*y+1
	if round(sqrt(z)) ** 2 == z:
		return True
		
def square(m):
	if round(sqrt(m)) ** 2 == m:
		return True

x = int(input())
if triangular(x) and square(x):
	print ("Both")
elif square(x):
	print ("Square")
elif triangular(x):
	print ("Triangular")
else:
	print("Neither")
