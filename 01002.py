string = input("")
target = input("")
n = 0
r = 0
i = 0
while (r!=-1):
	r = string.find(target, n)
	if (r != -1):
		n = r + 1
		i+=1
		
print (i)
