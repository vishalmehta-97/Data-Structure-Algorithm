'''This Question Better approach was with the 2 loops and down thier this is the most Optimal Solution'''

def secondLargest(nums):
    largest=nums[0]
    sLargest=min(nums)
    
    for i in range(len(nums)):
        if nums[i]>largest:
            sLargest=largest
            largest=nums[i]
        elif nums[i]>sLargest and nums[i]<largest:
                sLargest=nums[i]
    return sLargest

def SecondSmallest(nums):
    smallest=nums[0]
    secondsmallest=max(nums)

    for i in range(len(nums)):
        if nums[i]<smallest:
             secondsmallest=smallest
             smallest=nums[i]
        elif nums[i]>smallest and nums[i]<secondsmallest:
             secondsmallest=nums[i]
    return secondsmallest




nums=[1,3,4,7,7,5,2]
# print(secondLargest(nums))
print(SecondSmallest(nums))