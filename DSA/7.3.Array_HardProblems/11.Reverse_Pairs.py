'''Brute Force'''

def reversePairs(nums):
    n=len(nums)
    count=0
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>2*nums[j]:
                count+=1
    return count

nums=[1,3,2,3,1]
nums=[2,4,3,5,1]
# print(reversePairs(nums))


'''Optimal Approach'''
def merge(nums,low,mid,high):
    array=[]
    left=low
    right=mid+1
    
    while left<=mid and right<=high:
        if nums[left]>nums[right]:
            array.append(nums[right]) 
            right+=1
            
        else:
            array.append(nums[left]) 
            left+=1

    while left<=mid:
        array.append(nums[left])
        left+=1

    while right<=high:
        array.append(nums[right])
        right+=1

    for i in range(len(array)):
        nums[low+i]=array[i]

def countPairs(nums,low,mid,high):
    count=0
    right=mid+1
    for i in range(low,mid+1):
        while right<=high and nums[i]>2*nums[right]:
            right+=1
        count+=right-(mid+1)
    return count

def mergeSort(nums,low,high):
    count=0
    if low>=high:
        return count
    
    mid=(low+high)//2
    count+=mergeSort(nums,low,mid)
    count+=mergeSort(nums,mid+1,high)
    count+=countPairs(nums,low,mid,high)    
    merge(nums,low,mid,high)

    return count

def reversePairs_opts(nums):
    n=len(nums)
    return mergeSort(nums,0,n-1)

nums=[1,3,2,3,1]
nums=[2,4,3,5,1]
print(reversePairs_opts(nums))

