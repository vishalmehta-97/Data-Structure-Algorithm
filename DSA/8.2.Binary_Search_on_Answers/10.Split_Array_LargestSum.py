
def check(nums,mid,k):
    start=0
    count=1
    for i in range(len(nums)):
        if nums[i]>mid:
            return False
        start+=nums[i]
        if start>mid:
            count+=1
            start=nums[i]

        if count>k:
            return False  
    return True


def splitArray(nums,k):
    if len(nums)<k:
        return -1
    low=min(nums)
    high=sum(nums)

    while low<=high:

        mid=(low+high)//2

        if check(nums,mid,k):
            high=mid-1
        else:
            low=mid+1

    return low

nums=[7,2,5,10,8]
k=2
# nums=[10,20,30,40]
# k=2
nums=[1,4,4]
k=3
# nums=[10,5,20,25,17,23,2,9,4,13]
# k=7
print(splitArray(nums,k))