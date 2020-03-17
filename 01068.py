n = int(input())
 
full = {}

i = 0
while i<n:
	temp1 = input()
	temp = list(map(int, temp1.split()))
	full[temp1]= (temp[0]**2+temp[1]**2)
	i+=1
full = sorted(full)
for cnt in full:
	print (cnt)
