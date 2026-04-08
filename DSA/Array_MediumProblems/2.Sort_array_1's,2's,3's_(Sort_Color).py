def sort_colors(arr):
    n=len(arr)
    zeroes=0
    ones=0
    twos=0
    for i in range(n):
        if arr[i]==0:
            zeroes+=1
        elif arr[i]==1:
            ones+=1
        else:
            twos+=1

    for i in range(zeroes):
        arr[i]=0
    for j in range(zeroes,ones+zeroes):
        arr[j]=1
    for k in range(ones+zeroes,twos+ones+zeroes):
        arr[k]=2

    print(arr)


array=[2,0,2,1,1,0]
# sort_colors(array)

def sort_colors_Dutch_Flag_Algo(arr):
    n=len(arr)
    low=mid=0
    high=n-1

    # for _ in range(n): # or we can do this ""while mid<=high"":
    while mid<=high:    
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
    return arr
        
arr=[0,1,1,0,1,2,1,2,0,0,0]
print(sort_colors_Dutch_Flag_Algo(arr))
