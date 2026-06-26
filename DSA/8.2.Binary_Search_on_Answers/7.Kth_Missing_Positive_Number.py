''' Brute Force Approach '''

def findKth_Positive(arr,k):
    no=1000
    count=k
    for i in range(1,no+1):
        if i not in arr:
            count-=1
        
        if count==0:
            return i

arr=[2,3,4,7,11]
k=5
# print(findKth_Positive(arr,k))

''' Brute Force Approach '''

def findKth_Positive__(arr,k):

    for i in range(len(arr)):
        if arr[i]<=k:
            k+=1
        else:
            break
    return k
        
arr=[2,3,4,7,11]
k=5
arr=[1,2,3,4]
k=2
# print(findKth_Positive__(arr,k))

''''''

def findKth_Positive_(arr,k):
    n=len(arr)
    low=0
    high=n-1
    # ans=0
    while low<=high:
        mid=(low+high)//2
        cal=arr[mid]-(mid+1)

        if cal<k:
            low=mid+1
        else:
            high=mid-1 

    if high==-1:
        # return arr[low]-(arr[low]-k)
        return k
    elif low>n-1:
        # return arr[high]+(k-(arr[high]-(high+1)))   
        return high+k+1                            # this is after solving the above one or we can also do (low+k)
    else:
        # return arr[high]+(k-(arr[high]-(high+1)))
        return k+high-1
        
arr=[2,3,4,7,11]
k=5
# arr=[1,2,3,4]
# k=2
arr=[4,7,9]
k=3
print(findKth_Positive_(arr,k))

''' We can also do this intead of doing all the following returns for each conditions '''

def findKth_Positive_(arr,k):
    n=len(arr)
    low=0
    high=n-1
    # ans=0
    while low<=high:
        mid=(low+high)//2
        cal=arr[mid]-(mid+1)

        if cal<k:
            low=mid+1
        else:
            high=mid-1 

    return low+k
        
arr=[2,3,4,7,11]
k=5
# arr=[1,2,3,4]
# k=2
arr=[4,7,9]
k=3
print(findKth_Positive_(arr,k))

