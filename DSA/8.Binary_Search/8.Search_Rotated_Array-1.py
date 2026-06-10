def Search(nums,target):
    n=len(nums)
    low=0
    high=n-1

    while low<=high:
        mid=(low+high)//2

        if nums[mid]==target:
            return mid
        else:
            if nums[mid]>=nums[low]:
                if nums[low]<=target<=nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
 
            elif nums[mid]<nums[high]:
                if nums[mid]<=target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
    return -1


nums=[4,5,6,7,0,1,2]
nums=[5,1,3]
target=3
print(Search(nums,target))