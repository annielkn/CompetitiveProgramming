x = int(input(""))
y = [1000, 500, 100, 50, 20, 10]
for i in range(len(y)):
	while (x>=y[i]):
		print(y[i])
		x-=y[i]
