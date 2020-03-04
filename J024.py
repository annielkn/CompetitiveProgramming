import statistics 
n = int(input())
arr = [ int(input()) for i in range(n)]
print("%.3f" % statistics.mean(arr))
if isinstance(statistics.median(arr), int):
	print(statistics.median(arr))
else:
	print("%.1f" % statistics.median(arr))
print(statistics.mode(arr))
