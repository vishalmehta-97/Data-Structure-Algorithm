# 1st Approach
'''Brute Force'''

def rearrange_array_sign(nums):
    n=len(nums)
    pos=[]
    neg=[]

    for i in range(n):
        if nums[i]>=0:
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    
    for j in range(n//2):
        nums[2*j]=pos[j]
        nums[2*j+1]=neg[j]

    return nums


nums=[-1,1]
nums=[3,1,-2,-5,2,-4]
# print(rearrange_array_sign(nums))

'''Optimal'''

def rearrange_array_sign_optimal(nums):
    k=len(nums)
    arranged=[0]*k
    p=0
    n=1
    for i in range(k):
        if nums[i]>0:
            arranged[p]=nums[i]
            p+=2
        else:
            arranged[n]=nums[i]
            n+=2

    return arranged

nums=[3,1,-2,-5,2,-4]
# print(rearrange_array_sign_optimal(nums))

''' 2nd Way to do this (Here there are no fix didits of positive and negative so the remaining positives and negatives we have to put in the last)
eg.
    arr=[1,2,-4,-5,3,6]
    arr=[1,-4,2,-5,3,6]
'''

def rearrange_array_2nd_approach(arr):
    n=len(arr)
    pos=[]
    neg=[]
    for i in range(n):
        if arr[i]>0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    
    for j in range(n):
        

arr=[1,2,-4,-5,3,6]
arr=[1,2,-4,-5,3,7,17,7,7]
print(rearrange_array_2nd_approach(arr))

