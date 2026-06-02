## Brute is with the 3 loops

'''Better Approach'''

def maxProduct_Subarray(nums):
    n=len(nums)
    maxProduct=float('-inf')
    for i in range(n):
        product=1
        for j in range(i,n):
            product*=nums[j]
            maxProduct=max(product,maxProduct)

    return maxProduct


nums=[2,3,-2,4]
nums=[-2]
nums=[-2,0,-1]
print(maxProduct_Subarray(nums))

''' Optimal Approach '''

def maxProduct_Subarray(nums):
    n=len(nums)
    maxProduct=float('-inf')
    prefix=1
    suffix=1
    for i in range(n):
        if prefix==0:
            prefix=1
        if suffix==0:
            suffix=1
        prefix*=nums[i]
        suffix*=nums[n-1-i]
        maxProduct=max(maxProduct,max(prefix,suffix))
        
    return maxProduct
    

nums=[2,3,-2,4]
nums=[-2]
nums=[-2,0,-1]
print(maxProduct_Subarray(nums))