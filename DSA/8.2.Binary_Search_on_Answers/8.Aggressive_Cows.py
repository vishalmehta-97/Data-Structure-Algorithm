''' Brute Force Approach  '''

def checkTheCows(arr,i,k):
    count=1
    start=arr[0]
    for j in range(1,len(arr)):
        if arr[j]-start>=i:
            count+=1
            start=arr[j]

        if count>=k:
            return True
        
    return False

def aggressiveCows(arr,k):
    arr.sort()
    ans=0
    for i in range(1,max(arr)-min(arr)+1):
        if checkTheCows(arr,i,k):
            ans=i
    return ans

# arr=[0,3,4,7,10,9]
# k=4
arr=[4,2,1,3,6]
k=2
print(aggressiveCows(arr,k))


'''Binary Search'''

def checkTheCows_(arr,i,k):
    count=1
    start=arr[0]
    for j in range(1,len(arr)):
        if arr[j]-start>=i:
            count+=1
            start=arr[j]

        if count>=k:
            return True
        
    return False

def aggressiveCows_(arr,k):
    arr.sort()
    low=1
    high=((max(arr)-min(arr)))
  

    while low<=high:
        mid=(high+low)//2
        if checkTheCows_(arr,mid,k):
            low=mid+1
        else:
            high=mid-1

    return high


# arr=[0,3,4,7,10,9]
# k=4
arr=[4,2,1,3,6]
k=2
print(aggressiveCows(arr,k))