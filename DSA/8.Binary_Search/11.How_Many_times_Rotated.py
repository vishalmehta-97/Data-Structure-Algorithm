'''This is for the array where all the elements are unique and duplicates also'''

def rotated(nums):
    n=len(nums)
    low=0
    high=n-1
    ans=max(nums)
    index=-1

    while low<=high:
        mid=(low+high)//2

        while nums[low]==nums[mid] and nums[mid]==nums[high]:  ## By Adding this it will work for the duplicates as well
            low+=1
            high-=1  

        if nums[low]<=nums[high]:  
            if ans>nums[low]:
                ans=nums[low]
                index=low
            break

        if nums[mid]>=nums[low]:
            if ans>nums[low]:
                ans=nums[low]
                index=low
            low=mid+1

        elif nums[mid]<=nums[high]:
            if ans>nums[mid]:
                index=mid
            high=mid-1

    return index

nums=[3,3,3,1,3,3,3,3,3,]
print(rotated(nums))