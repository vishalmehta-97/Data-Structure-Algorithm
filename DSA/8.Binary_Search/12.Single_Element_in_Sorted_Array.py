''' Brute Force '''

def singleElement_Brute(nums):
    n=len(nums)
    for i in range(n):
        if i==0:
            if nums[i]!=nums[i+1]:
                return nums[0]
        elif i==n-1:
            if nums[i-1]!=nums[i]:
                return nums[n-1]
        else: 
            if nums[i-1]!=nums[i] and nums[i+1]!=nums[i]:
                return nums[i]  
    return -1

nums=[1,1,2,2,3,3,4,5,5,6,6]
# print(singleElement_Brute(nums))

''' Optimal Approach '''
def singleElement(nums):
    n=len(nums)
    if n==1:
        return nums[0]
    if nums[0]!=nums[1]:
        return nums[0]
    if nums[n-1]!=nums[n-2]:
        return nums[n-1]
    
    low=1
    high=n-2
    while low<=high:
        mid=(low+high)//2

        if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
            return nums[mid]
        else:
            if mid%2!=0:
                if nums[mid-1]==nums[mid]:
                    low=mid+1
                else:
                    high=mid-1
            elif mid%2==0:

                if nums[mid+1]==nums[mid]:
                    low=mid+1
                else:
                    high=mid-1

    return -1

nums=[1,1,2,2,3,3,4,5,5,6,6]
# nums=[3,3,7,7,10,11,11]
# nums=[1]
# nums=[1,1,2]
nums=[1,2,2]
print(singleElement(nums))

