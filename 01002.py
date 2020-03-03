string = input("")
target = input("")
n = -1
r = 0
i = 0
while (r!=-1):
	r = string.find(target, n+1)
	i+=1
	print(r)
	if (r != -1):
		n = r
		
print (i-1)
