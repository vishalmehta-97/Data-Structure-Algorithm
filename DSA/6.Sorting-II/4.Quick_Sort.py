# def quickSort(array,l,h):
#     if l>=h:
#         return array
    
#     pivot=array[l]
#     i=l
#     j=h

#     while i<=j:
#         while array[i]<=pivot and i<=h:
#             i+=1
#         while array[j]>pivot and j>=l:
#             j+=1
#         if array[i]>pivot and array[j]<pivot:
#             array[i],array[j]=array[j],array[i]
#             i+=1
#             j+=1
        
#         array[l],array[j]=array[j],array[l]
#         return j
#     quickSort(array,l,j-1)
#     quickSort(array,h,j+1)
# array=[4,6,2,5,7,9,1,3]
# n=len(array)
# quickSort(array,0,n-1)


def quickSort(arr, low, high):
    if low < high:
        pivotIndex = partition(arr, low, high)
        quickSort(arr, low, pivotIndex - 1)
        quickSort(arr, pivotIndex + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1

            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
    
arr = [10, 7, 8, 9, 1, 5]
# quickSort(arr, 0, len(arr) - 1)
# print(arr)


n=5
for i in range(n):
    
    for j in range(i):
        print(j,end=" ")
    print()