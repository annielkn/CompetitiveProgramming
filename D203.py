#clap N
x = 1
N = int(input(""))
while x < 101:
	if (x % N == 0):
		print ("Clap", end = " ")
	elif (x % 10 == N):
		print ("Clap", end = " ")
	elif (x - N * 10 > 0 and x - 70 < 10):
		print ("Clap", end = " ")
	elif (x % 10 == 0):
		print (x, end = "\n")
	else:
		print (x, end = " ")
	x+=1
	
