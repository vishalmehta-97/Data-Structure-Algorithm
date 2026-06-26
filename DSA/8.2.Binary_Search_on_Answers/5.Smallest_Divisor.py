'''Brute Force Approach'''
## Instead of doing the condition to get the reminder we can use seil function with math library
def smallestDivisor(nums,t):
    maxi=max(nums)
    for i in range(1,maxi+1):
        r=0
        for j in range(len(nums)):
            if nums[j]%i!=0:
                r+=(nums[j]//i)+1
            else:
                r+=nums[j]//i
        if r<=t:
            return i


nums=[1,2,5,9]
t=6
print(smallestDivisor(nums,t))

'''Optimal Approach'''

def totalReminder(nums,mid):
    r=0
    for j in range(len(nums)):
        if nums[j]%mid!=0:
            r+=(nums[j]//mid)+1
        else:
            r+=nums[j]//mid
    return r

def smallestDivisor_(nums,t):
    if len(nums)>t:  ## No Divisor
        return -1
    low=1
    high=max(nums)
    ans=0
    while low<=high:
        mid=(low+high)//2

        if totalReminder(nums,mid)<=t:
            ans=mid
            high=mid-1
        else:
            low=mid+1

    return ans # we can also return low
        
nums=[1,2,5,9]
t=7
nums=[44,22,33,11,1]
t=5
print(smallestDivisor_(nums,t))