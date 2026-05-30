def dup_values(arr, dup):
    for i in arr:
        if arr.count(i) > 1 and i not in dup:
            dup.append(i)
            
arr = list(map(int, input().split()))
dup = []
dup_values(arr, dup)
print(*dup)