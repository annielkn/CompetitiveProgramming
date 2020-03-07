x = int(input())
half = int((x-1)/2)
fixedhalf = int((x-1)/2)
i = 0
t = 0
while i < x:
	for n in range(abs(half)): 
		print(" ", end="")
	if (i == 0 or i == x-1): 
		print ("#")
	else:
		print ("#", end='')
		
		t = i*2-1
		if i > fixedhalf:
			t = t - 4 * (i - fixedhalf)
		
		for n in range(t):
			print(" ", end='')
		
		print ("#")
		
	half -= 1
	i += 1
