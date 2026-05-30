
def array_search(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i, target
    return -1

n = int(input())
target = int(input())
arr = list(map(int, input().split()))
print(array_search(arr, target))
