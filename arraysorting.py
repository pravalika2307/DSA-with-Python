n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(*arr) # gives o/p as : 12 27 62 73 99 instead of : [12, 27, 62, 73, 99]