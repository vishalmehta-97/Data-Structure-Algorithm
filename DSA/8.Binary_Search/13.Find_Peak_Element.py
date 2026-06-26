'''Brute Force Approach'''

def peakElement1(nums):
    n=len(nums)
    max=-1
    ind=-1
    for i in range(n):
        if nums[i]>max:
            max=nums[i]
            ind=i

    return ind

# nums=[1,2,3,1]
nums=[1,2,1,3,5,6,4]
# print(peakElement1(nums))

## this is also a brute force approach

def peakElement2(nums):
    n=len(nums)
    peak=-1
    for i in range(n):
        if i==0 and nums[i]>nums[i+1]:
            peak=max(peak,i)
        elif i==n-1 and nums[i]>nums[i-1]:
            peak=max(peak,i)
        else:
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                peak=max(peak,i)
    
    return peak  ## Here i have returned the top peak index but we can do the same for the any peak in the array
    
nums=[1,2,3,1]
nums=[1,2,1,3,5,6,4]
# print(peakElement2(nums))

''' Optimal Approach '''
## This will also work for more then 1 peaks
def peakElement(nums):
    n=len(nums)
    low=1
    high=n-2

    if n==1:
        return 0
    if nums[0]>nums[1]:
        return 0
    if nums[n-1]>nums[n-2]:
        return n-1
    
    while low<=high:    
        mid=(low+high)//2
        if nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
            return mid
        else:
            if nums[mid-1]>nums[mid]:
                high=mid-1
            else:
                low=mid+1

    return -1

nums=[1,2,1,3,5,6,4]
# nums=[1]
nums=[1,2]
# nums=[1,2,3,4,5,6,7,8,5,1]
nums=[1,5,1,2,1]
print(peakElement(nums))