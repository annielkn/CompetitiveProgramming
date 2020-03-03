string = input("")
target = input("")
n = 0
r = 0
i = 0
while (r!=-1):
	r = string.find(target, n)
	i+=1
	print(r)
	if (r != -1):
		n = r + 1
		
print (i-1)
