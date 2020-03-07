temp = list(map(int, input().split()))
N = temp [0]
M = temp [1]
narr = list(map(int, input().split()))
marr = list(map(int, input().split()))
merge = narr + marr
merge.sort()
print (*merge, end = "")
