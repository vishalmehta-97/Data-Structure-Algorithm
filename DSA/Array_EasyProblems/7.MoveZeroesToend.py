'''Brute Force'''

# def moveZeroes(nums) -> None:
#     n=len(nums)
#     temp=[]
#     for i in range(n):
#         if nums[i]!=0:
#             temp.append(nums[i])
#     print(temp)
#     nums[:len(temp)]=temp[:]
#     for j in range(len(temp),n):
#         nums[j]=0
#     return nums
# nums=[0,1,0,3,12]
# print(moveZeroes(nums))



'''Optimal'''
def moveZeroes(nums) -> None:
    n=len(nums)
    ii=0
    for i in range(n):
        if nums[i]!=0:
            nums[ii]=nums[i]
            ii+=1
    for j in range(ii,n):
        nums[j]=0

    return nums
       

nums=[0,1,0,3,12]
nums=[1,0,2,3,2,0,0,4,5,1]
print(moveZeroes(nums))


def moveZeroess( nums):
    j = -1
    for i in range(len(nums)):
        if nums[i] == 0:
            j = i
            break
    if j == -1:
        return
    
    for i in range(j + 1, len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums


nums = [0, 1, 0, 3, 12]
print(moveZeroess(nums))