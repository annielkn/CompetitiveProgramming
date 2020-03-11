#factors
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

x = int(input())
t = x
factors = []
primef = []
i = 2
if prime(t):
	print (str(t)+"="+str(t))
else:
	while prime(t) == False:
		if i == sqrt(x):
			factors.append(i)
		while t % i == 0:
			factors.append(i)
			t = int(t/i)
		i += 1
	factors.append(t)

	for n in range(len(factors)):
		if prime(factors[n]):
			primef.append(factors[n])
	primef = sorted(primef)
	print (str(x)+"=", end = "")
	for n in range(len(primef)-1):
		print (primef[n], end = "*")
	print (primef[len(primef)-1])
