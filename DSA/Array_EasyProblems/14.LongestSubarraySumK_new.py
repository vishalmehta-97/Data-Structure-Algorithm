'''This Is Brute (O(n^3)) But it can be improved '''
def longestSubnumsay_Sum(nums,k):
    n=len(nums)
    max_length=0
    for i in range(n):
        for j in range(i,n+1):
            sum=0
            for l in range(i,j):
                sum+=nums[l]
            if sum==k:
                max_length=max(max_length,j-i)
    return max_length

nums=[1,2,3,1,1,4,1,1,1]
k=3
# print(longestSubnumsay_Sum(nums,k))


'''This Is improved Brute (O(n^2)) '''


def longestSubnumsay_Sumk(nums,k):
    n=len(nums)
    max_length=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=nums[j]
            if sum==k:
                max_length=max(max_length,j-i+1)
    return max_length

nums=[1,2,3,1,1,4,1,1,1]
k=3
# print(longestSubnumsay_Sumk(nums,k))

## Same thing brute in 0(n^2)

def subnumsay(nums,k):
    n=len(nums)
    max_length=0

    for i in range(n):
        sum=0 
        for j in range(i,n):
            sum+=nums[j]
            length=0
            if sum==k:
                length=j-i+1
                if length>max_length:
                    max_length=length

    return max_length

nums=[1,2,3,1,1,1,1,4,2,3]
nums=[1,2,3,1,1,4,1,1,1]
k=3
# print(subnumsay(nums,k))


'''Better Approach'''
# This Approach will optimal when we have all (Positive's,Negative's and Zero) integers
def longestSubnumsay_sum_Hash(nums,k):
    n=len(nums)
    hash={}
    sum=0
    max_length=0
    for i in range(n):
        length=0
        sum+=nums[i]
        if sum==k:
            length=i+1
            max_length=max(length,max_length)

        prefix=sum-k

        if prefix in hash:
            length=i-hash.get(prefix)
            max_length=max(max_length,length)
        
        if sum not in hash:
            hash[sum]=i

    return max_length
        
nums=[1,2,3,1,1,4,1,1,1]
nums=[1,2,3,1,1,1,1,4,2,3]
nums=[2,0,0,3]
nums=[10,5,2,7,1,9]
nums=[-3,2,1]
nums=[-1,1,1]
k=1
# print(longestSubnumsay_sum_Hash(nums,k))


'''Optimal Approach (but this work only when we have all positives and zeroes in the array)'''

def longestSubnumsay_sum_Optimal(nums,k):
    n=len(nums)
    i=j=0
    sum=0
    max_length=0
    while i<n and j<n :
        length=0
        sum+=nums[j]
        while sum>k:
            sum-=nums[i]
            i+=1
        if sum==k:
            length=j-i+1
            max_length=max(length,max_length)
        j+=1
    return max_length
        
nums=[1,2,3,1,1,1,1,3,3]
nums=[10,5,2,7,1,9]
nums=[1,2,3,1,1,4,1,1,1]
k=3
# print(longestSubnumsay_sum_Optimal(nums,k))


## Same Code but with more better and stable 

def opt(nums,k): 
    n=len(nums)
    i=j=0
    total=nums[0]
    max_length=0

    while j<n:
        while i<=j and total>k:
            total-=nums[i]
            i+=1
        if total==k:
            max_length=max(max_length,j-i+1)
        j+=1
        if j<n:
            total+=nums[j]
    return max_length
nums=[1,2,3,1,1,1,1,3,3]
k=6
nums=[10,5,2,7,1,9]
k=15
print(opt(nums,k))