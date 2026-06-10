''' With Iteration '''

def lowerBound(nums,x):
    n=len(nums)
    low=0
    high=n-1
    ans=len(nums)
    while low<=high:
        mid=(low+high)//2

        if nums[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
        
    return ans
    
    

nums=[1,3,5,6,7,8,10,12,15,19]
nums=[1,2,3,3,5,8,8,10,10,11]

print(lowerBound(nums,10))

''' Recursion '''

def lowerBound(nums,low,high,x,ans):
    if high<low:
        return ans
    
    mid=(low+high)//2
    if nums[mid]>=x:
        ans=mid
        return lowerBound(nums,low,mid-1,x,ans)
    else:
        return lowerBound(nums,mid+1,high,x,ans)

nums=[1,3,5,6,7,8,10,12,15,19]
nums=[1,2,3,3,5,8,8,10,10,11]
n=len(nums)
low=0
high=n-1
x=10
# print(lowerBound(nums,low,high,x,len(nums)))