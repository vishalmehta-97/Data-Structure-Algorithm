def Search(nums,target):
    n=len(nums)
    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2

        if nums[mid]==target:
            return True
        else:
            if nums[mid]==nums[low] and nums[mid]==nums[high]:
                low+=1
                high-=1
                continue

            if nums[mid]>=nums[low]:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
 
            elif nums[mid]<=nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
    return False


nums=[2,5,6,0,0,0,1,2]
nums=[3,1,2,3,3,3,3]
nums=[1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]
target=13
print(Search(nums,target))