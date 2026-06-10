def searchInsert_Position(nums,x):
    n=len(nums)
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2

        if nums[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1

    return ans

nums=[1,2,4,7]
nums=[1,3,5,6]
x=7
print(searchInsert_Position(nums,x))
