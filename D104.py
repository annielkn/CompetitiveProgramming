from math import sqrt
y = 0
numbers = [int(n) for n in input().split()]
x = numbers[1]*numbers[1]-4*numbers[0]*numbers[2]
if x < 0:
	print ("None")
elif x == 0:
	y = (numbers[1]*(-1)+sqrt(x))/(2*numbers[0])
	print ("%.3f" % round(y,3))
elif x > 0:
	a = (numbers[1]*(-1)+sqrt(x))/(2*numbers[0])
	#print ("%.3f" % round(y,2), end = " ")
	b = (numbers[1]*(-1)-sqrt(x))/(2*numbers[0])
	if (a<b):
		print ("%.3f" % round(a,3), end = " ")
		print ("%.3f" % round(b,3))
	elif (a>b):
		print ("%.3f" % round(b,3), end = " ")
		print ("%.3f" % round(a,3))
	#print ("%.3f" % round(y,2))
