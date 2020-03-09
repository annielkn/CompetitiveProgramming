from math import sqrt
from math import ceil
temp = input()
x1 = ord(temp[0])-96
y1 = int(temp[1])
#print (x1, y1)
temp = input()
x2 = ord(temp[0])-96
y2 = int(temp[1])
a = abs(x1-x2)
b = abs(y1-y2)

cnt = 0
cnt = min(a, b)
n = cnt
#print (a, b, cnt)
if a == b: 
	print(a)
else: 
	print(cnt+abs(n-a)+abs(n-b))
