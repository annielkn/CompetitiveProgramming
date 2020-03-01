i=0
x=0
y=1
temp = 0

w = int(input(""))

while i < w:
	temp = x + y
	x = y
	y = temp
	i+=1

print (x)
