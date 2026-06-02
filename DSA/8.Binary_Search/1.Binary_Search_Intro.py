'''Binary Search Interative Code'''

def binarySearch(nums,n,target):
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        
        else:
            if target>nums[mid]:
                low=mid+1
            else:
                high=mid-1

    return -1

nums=[3,4,6,7,9,12,16,17]
n=len(nums)
# print(binarySearch(nums,n,17))


'''Binary Search Recursive Code'''

def binarySearch_(nums,low,high,target):
    if high<low:
        return -1
    
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    else:
        if target>nums[mid]:
            return binarySearch_(nums,mid+1,high,target)
        else:
            return binarySearch_(nums,low,mid-1,target)
    

nums=[3,4,6,7,9,12,16,17]
n=len(nums)
low=0
high=n-1
print(binarySearch_(nums,low,high,12))


## time Complexity=log n (base2) 

f'''
Overflow Problem when the array has the last index which 
is the maximum no of elements which we can store so that time 
{(high+low)/2}for mid will be very high value which maybe we can't 
store,

So that time we use {low + (high-low)/2}

'''
