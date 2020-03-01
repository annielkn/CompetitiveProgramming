from math import sqrt
y = 0
numbers = [int(n) for n in input().split()]
x = numbers[1]*numbers[1]-4*numbers[0]*numbers[2]
if x < 0:
	print ("None")
elif x == 0:
	y = (numbers[1]*(-1)+sqrt(x))/(2*numbers[0])
	print ("%.3f" % round(y,2))
elif x > 0:
	y = (numbers[1]*(-1)+sqrt(x))/(2*numbers[0])
	print ("%.3f" % round(y,2))
	y = (numbers[1]*(-1)-sqrt(x))/(2*numbers[0])
	print ("%.3f" % round(y,2))
