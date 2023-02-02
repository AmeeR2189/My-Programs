def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = list(map(int,input().split()))
print("Sorted array:", selection_sort(arr))


##################################################
def selectionsort(n,arr):
    if n==0:
        return
    maxind=findmax(arr,n)
    arr[maxind],arr[n]=arr[n],arr[maxind]
    selectsort(n-1,arr)

n=int(input())


.
