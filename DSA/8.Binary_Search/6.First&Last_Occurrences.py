'''Brute Using Linear Search'''

def linear_FandL(nums,x):
    first=-1
    last=-1
    for i in range(len(nums)):
        if nums[i]==x:
            if first==-1:
                first=i

            last=i
        
    return [first,last]

nums=[2,4,6,8,8,8,11,13]
nums=[5,7,7,8,8,10]
x=8 
# nums=[5,7,7,8,8,10,12,15,16,16,17]
# x=16
print(linear_FandL(nums,x))


''' First have done the front and last occurance seprately '''

class Solution:
# First
    def first_occurance(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        first_occ=-1

        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                first_occ=mid
                high=mid-1

            elif nums[mid]>target:
                high=mid-1

            else:
                low=mid+1

        return first_occ

    # Last 

    def last_occurance(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        last_occ=-n 

        while low<=high:
            mid=(low+high)//2

            if nums[mid]==target:
                last_occ=mid
                low=mid+1

            elif nums[mid]>target:
                high=mid-1

            else:
                low=mid+1

        return last_occ

    ## First And Last

    def searchRange(self,nums,target):
        first=self.first_occurance(nums,target)
        last=self.last_occurance(nums,target)

        return [first,last]
    
'''Maybe More Structured'''

class Solution:
# First
    def first_occurance(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        first_occ=n

        while low<=high:
            mid=(low+high)//2
            if nums[mid]>=target:
                first_occ=mid
                high=mid-1

            else:
                low=mid+1

        if first_occ==n or nums[first_occ]!=target :
            return -1
        return first_occ

    # Last 

    def last_occurance(self,nums,target):
        n=len(nums)
        low=0
        high=n-1
        last_occ=n

        while low<=high:
            mid=(low+high)//2

            if nums[mid]>target:
                last_occ=mid
                high=mid-1

            else:
                low=mid+1
      
        return last_occ-1

    ## First And Last

    def searchRange(self,nums,target):
        first=self.first_occurance(nums,target)

        if first==-1:
            return [-1,-1]
        return [first,self.last_occurance(nums,target)]


s=Solution()

nums = [5,7,7,8,8,10]
nums = []
target=0
print(s.searchRange(nums,target))
    
'''Using Basic Binary Search Concept'''

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