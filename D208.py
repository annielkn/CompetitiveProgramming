y = int(input())
arr = list(map(int, input().split()))
print (max(arr))
arr.remove(max(arr))
print (max(arr))
