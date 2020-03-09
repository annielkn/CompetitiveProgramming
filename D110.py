from math import sqrt
from math import ceil
temp = input()
x1 = ord(temp[0])-96
y1 = int(temp[1])
temp = input()
x2 = ord(temp[0])-96
y2 = int(temp[1])
print(ceil(sqrt((y2-y1)**2+(x2-x1)**2))-1)
