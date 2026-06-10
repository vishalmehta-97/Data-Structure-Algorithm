''' With Iteration '''

def upperBound(nums,x):
    n=len(nums)
    low=0
    high=n-1
    ans=len(nums)
    while low<=high:
        mid=(low+high)//2

        if nums[mid]>x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
        
    return ans

nums=[1,3,5,6,7,8,10,12,15,19]
nums=[2,3,6,7,8,8,11,11,11,12]
print(upperBound(nums,6))

''' Recursion '''

def upperBound_(nums,low,high,x,ans):
    if low>high:
        return ans
    
    mid=(low+high)//2
    if nums[mid]>x:
        ans=mid
        return upperBound_(nums,low,mid-1,x,ans)
    else:
        return upperBound_(nums,mid+1,high,x,ans)

nums=[1,3,5,6,7,8,10,12,15,19]
nums=[2,3,6,7,8,8,11,11,11,12]
n=len(nums)
low=0
high=n-1

print(upperBound_(nums,low,high,6,n))