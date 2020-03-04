import statistics 
n = int(input())
arr = [ int(input()) for i in range(n)]
print("%.3f" % statistics.mean(arr))
if statistics.median(arr) == int(statistics.median(arr)):
	print(int(statistics.median(arr)))
else:
	print("%.1f" % statistics.median(arr))
print(statistics.mode(arr))
