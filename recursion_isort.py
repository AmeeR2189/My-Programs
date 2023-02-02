def recursion_insertion_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        key = arr[-1]
        arr = recursion_insertion_sort(arr[:-1])
        for i in range(len(arr)):
            if arr[i] > key:
                arr.insert(i, key)
                break
        else:
            arr.append(key)
        return arr


arr=list(map(int,input().split()))
print(recursion_insertion_sort(arr))