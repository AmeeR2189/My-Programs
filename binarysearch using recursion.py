def binary_search(arr, low, high, x):
    if low <= high:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1

arr = list(map(int,input().split()))
x = int(input())
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print(result)
else:
    print("Element is not present in array")
