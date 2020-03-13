#d205 
from math import sqrt
def prime(x):
	i = 1
	if x == 2:
		return True
	elif x > 2:
		while i <= sqrt(x):
			i+=1
			if x % i == 0:
				return False
				break
		else:
			return True
			
def find_factors(m):
	n = m #m i s the number where we find factors for m, but we are not going to directly change m
	i = 1
	v = 0 #maximum value
	while i <= n:
		i+=1
		while n % i == 0:
			if i >= v and prime(i) != False: 
				v = i
				if (n / i == 1):
					print (i)
				else:
					print (i, end = "*")
				n = n / i
				
x = int(input(""))
if prime(x) == True:
	print (str(x)+"="+str(x))
else:
	print (x, end = "=")
	find_factors(x)
