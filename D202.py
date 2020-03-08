from math import sqrt
x = int(input())
factors = []
i = 1
while i <= sqrt(x):
	if i == sqrt(x):
		factors.append(i)
	elif x % i == 0:
		factors.append(i)
		factors.append(int(x/i))
	i += 1
factors = sorted(factors)
for n in range(len(factors)):
	print (factors[n])
