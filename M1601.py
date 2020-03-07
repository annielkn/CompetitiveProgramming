# your code goes here
x = int(input())
tot = 1
cnt = 2000
dow = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
while cnt < x:
	if (cnt % 4 == 0 and (cnt%400 == 0 or cnt %100 !=0)) :
		tot += 2
	else:
		tot +=1
	cnt +=1
tot = tot % 7
print (dow[tot])
