def checkAllocations(nums,mid,s):
    count=1
    sum=0

    for i in range(len(nums)):
        if nums[i]>mid:
            return False
        
        sum+=nums[i]
        if sum>mid:
            count+=1
            sum=nums[i]

        if count>s:
            return False
        
    return True



def allocateBooks(nums,s):

    if len(nums)<s:
        return -1

    low=min(nums)
    high=sum(nums)

    while low<=high:
        mid=(low+high)//2

        if checkAllocations(nums,mid,s):
            high=mid-1
        else:
            low=mid+1

    return low

# nums=[12,34,67,90]
# m=2
nums=[25, 46, 28, 49, 24]
m=4
nums=[15, 17, 20]
m=5
print(allocateBooks(nums,m))