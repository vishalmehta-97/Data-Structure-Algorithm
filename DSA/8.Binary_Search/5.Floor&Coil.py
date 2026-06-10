''' Floor --> Largest no <= x '''

def floor(nums,x):
    n=len(nums)
    low=0
    high=n-1
    floor=-1

    while low<=high:
        mid=(low+high)//2
    
        if nums[mid]<=x:
            floor=nums[mid]
            low=mid+1
        else:
            high=mid-1

    return floor


nums=[10,20,30,40,50]
x=25
nums=[10,15,17.21,25,29,31]
x=27
print(floor(nums,x)) 


''' Ceil --> Smallest no >= x '''

def ceil(nums,x):
    n=len(nums)
    high=n-1
    low=0
    Ceil=-1

    while low<=high:
        mid=(low+high)//2
    
        if nums[mid]>=x:
            Ceil=nums[mid]
            high=mid-1
        else:
            low=mid+1

    return Ceil

nums=[10,20,30,40,50]
x=25 
nums=[10,15,17.21,25,29,31]
x=27
print(ceil(nums,x)) 


''' If we want to do this in the same code '''

def FloorandCeil(nums,x):
    n=len(nums)
    low=0
    high=n-1
    floor=-1
    ceil=-1

    while low<=high:
        mid=(low+high)//2

        if nums[mid]==x:
            return nums[mid],nums[mid]
        
        elif nums[mid]>x:
            ceil=nums[mid]
            high=mid-1

        else:
            floor=nums[mid]
            low=mid+1

    return floor,ceil

nums=[10,15,17.21,25,29,31]
x=27
print(FloorandCeil(nums,x))
