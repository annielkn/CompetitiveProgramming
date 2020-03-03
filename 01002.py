string = input("")
target = input("")
n = 0
r = 0
i = 0
while (r!=-1):
	r = string.find(target, n+1)
	i+=1
	if (r != -1):
		n = r
		
print (i)
