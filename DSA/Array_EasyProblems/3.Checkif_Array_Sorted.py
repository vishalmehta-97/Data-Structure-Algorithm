# def CheckSortednumsay(nums):
#     for i in range(len(nums)-1):
#         if nums[i]<=nums[i+1]:
#                 pass
#         elif nums[i]>nums[i+1]:
#             rotated=nums[i+1:len(nums)]
#             print(rotated)
#             for i in range(0,len(rotated)-1):
#                 if rotated[i]<rotated[i+1] and rotated[i+2]<nums[i] and rotated[len(rotated)-1]<nums[0]:
#                     pass
#                 else:
#                     return False
#             return True
#         else:
#             return False
#     return True
# nums=[2,1,3,4]
# print(CheckSortednumsay(nums))


def CheckSortedArray(nums):
    count=0
    n=len(nums)
    for i in range(n):
        if nums[i]>nums[(i+1)%n]:
            count+=1    
    return count<=1
        
nums=[10,1,1,10]
nums=[2,1,3,4]
print(CheckSortedArray(nums))
