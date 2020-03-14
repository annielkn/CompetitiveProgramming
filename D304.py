x = input()
"""arr = [input() while i != ""]"""
arr = ["_" for i in range(len(x))]

while arr != x:
	string = input()
	#print (string)
	i = 0
	while i<len(x):
			#print (arr[cnt], end="")
		if (x[i] == string):
			arr[i] = string
		i+=1
		#else:
			#print ("_", end="")
	for t in range(len(arr)):
		print(arr[t], end = "")
	print ()
