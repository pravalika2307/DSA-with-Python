def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 # if target not in arr
    
arr = list(map(int, input().split()))
target = int(input())
print(linear_search(arr, target))