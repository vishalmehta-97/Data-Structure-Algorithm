def minimum(nums):
    n=len(nums)
    low=0
    high=n-1
    mini=max(nums)

    while low<=high:
        mid=(low+high)//2
        
        mini=min(mini,nums[mid])  ## This line is not that much important

        if nums[low]<=nums[high]:  ## This is checking and if search space is already sorted then the arr[low] will be the lowest 
            mini=min(mini,nums[low])
            break

        if nums[mid]>=nums[low]:
            mini=min(mini,nums[low])
            low=mid+1

        elif nums[mid]<=nums[high]:
            mini=min(mini,nums[mid])
            high=mid-1

    return mini

nums=[4,5,6,7,0,1,2]
# nums=[3,4,5,1,2]
print(minimum(nums))

