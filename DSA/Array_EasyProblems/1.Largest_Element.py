# arr = list(map(int,input().split()))
# print(arr)

def largestElement(arr):
    high=arr[0]
    for i in range(len(arr)):
        if arr[i]>high:
            high=arr[i]
    return high

arr=[3,2,1,5,2]
arr=[30,27,11,54,21,30,25,14,57,255]
print(largestElement(arr))