'''Brute Force'''

def countInversion(nums):
    n=len(nums)
    count=0

    for i in range(n):
        for j in range(i+1,n):
            if nums[i]>nums[j]:
                count+=1
    return count


nums=[5,3,2,4,1]
# print(countInversion(nums))


''' Optimal Approach (Merge Sort Approach) '''

def merge(nums,low,mid,high):
    count=0
    array=[]
    left=low
    right=mid+1

    while left<=mid and right<=high:
        if nums[left]>nums[right]:
            count+=(mid-left+1)
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
    return count

def mergeSort(nums,low,high):
    count=0
    if low>=high:
        return count
    
    mid=(low+high)//2
    count+=mergeSort(nums,low,mid)
    count+=mergeSort(nums,mid+1,high)    

    count+=merge(nums,low,mid,high)

    return count

def numberOfInversions(nums):
    n=len(nums)
    return mergeSort(nums,0,n-1)

nums=[5,3,2,4,1]
print(numberOfInversions(nums))


## we can also do this with count but above one is more optimal in coding 

count = 0
def merge(nums, low, mid, high):
    global count
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            count += (mid - left + 1)
            right += 1

    while left <= mid:
        temp.append(nums[left])
        left += 1

    while right <= high:
        temp.append(nums[right])
        right += 1

    for i in range(len(temp)):
        nums[low + i] = temp[i]

def mergeSort(nums, low, high):
    if low >= high:
        return
    
    mid = (low + high) // 2
    mergeSort(nums, low, mid)
    mergeSort(nums, mid + 1, high)
    merge(nums, low, mid, high)

def numberOfInversions(nums):
    global count
    count = 0
    mergeSort(nums, 0, len(nums) - 1)
    return count

nums = [5,3,2,4,1]
print(numberOfInversions(nums))