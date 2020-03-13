temp = list(map(int, input().split()))
n = temp[0]
m = temp[1]
mid = int(m/2)
shit = []
shit.append(mid)
x = 1
while x <= int((n-1)/2):
	if ((mid+x != 0) and (mid-x != 0)):
		shit.append(mid+x)
		shit.append(mid-x)
	x += 1
	
shit = sorted(shit)
if (sum(shit) < m):
	shit[len(shit)-1] += (m-sum(shit))
if (sum(shit) > m):
	shit[0] += (m-sum(shit))
if (len(shit)-1 == n):
	shit[len(shit)-2] += shit[len(shit)-1] 
if (len(shit)+1 == n):
	shit.append(0)
for i in range(len(shit)):
	print (shit[i], end = " ")
