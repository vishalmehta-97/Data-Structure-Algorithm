def first_occurance(nums,target):
    n=len(nums)
    low=0
    high=n-1
    first=-1
    while low<=high:
        mid=(low+high)//2

        if nums[mid]==target:
            first=mid
            high=mid-1
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1 
    return first

def last_occurance(nums,target):
    n=len(nums)
    low=0
    high=n-1
    last=-1
    while low<=high:
        mid=(low+high)//2

        if nums[mid]==target:
            last=mid
            low=mid+1
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return last

def occurances(nums,target):

    first=first_occurance(nums,target)
    if first==-1:
        return [-1,-1]
    last=last_occurance(nums,target)
    
    return [first,last]

nums=[2,8,8,8,8,11,13]
target=8
print(occurances(nums,target))



'''
Just like the previous question we have used just
the basic binary search to get the first and last occurance
and then we have just done this

total_count= last_occ index-first_occ index + 1

'''
class Solution:
    def first_occurance(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        first=-1
        while low<=high:
            mid=(low+high)//2

            if nums[mid]==target:
                first=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1 
        return first

    def last_occurance(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        last=-1
        while low<=high:
            mid=(low+high)//2

            if nums[mid]==target:
                last=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return last

    def countOccurrences(self, nums, target):
        first=self.first_occurance(nums,target)
        if first==-1:
            return 0
        last=self.last_occurance(nums,target)
        
        return last-first+1


