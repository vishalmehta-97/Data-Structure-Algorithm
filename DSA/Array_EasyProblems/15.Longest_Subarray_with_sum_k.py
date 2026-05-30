'''This is The Better Approach (the brute will be with 3 loops)''' 

def Longest_Subarray_sumK(nums,k):
    n=len(nums)
    max_length=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=nums[j]
            length=0
            if sum==k:
                length=j-i+1
                max_length=max(length,max_length)

    return max_length

nums=[1,2,3,1,1,1,1,3,3]
k=3
print(Longest_Subarray_sumK(nums,k))


'''Optimal Approach(Using Hash)'''

def Longest_Subarray_sumK(nums,k):
    n=len(nums)
    prefix_sum={}
    sum=0
    max_length=0
    for i in range(n):
        sum+=nums[i]
        if sum==k:
            max_length=max(max_length,i+1)
        else:
            if sum-k in prefix_sum:
                max_length=max(max_length,i-prefix_sum.get(sum-k))

            elif sum not in prefix_sum:
                prefix_sum[sum]=i
    
    return max_length

nums=[1,2,3,1,1,1,1,3,3]
k=3
# nums=[10, 5, 2, 7, 1, 9]
# k=15
print(Longest_Subarray_sumK(nums,k))