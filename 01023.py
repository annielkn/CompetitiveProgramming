arr = list(map(int, input().split()))
N = arr[0]
K = arr[1]
temp = list(map(int, input().split()))
mini = abs(temp[0]-K)
minikey = temp[0]
for i in range(len(temp)):
	x = abs(temp[i]-K)
	if (x<mini):
		mini = x
		minikey = temp[i]
	if (x==mini and temp[i]>minikey):
			minikey = temp [i]
print(minikey)
