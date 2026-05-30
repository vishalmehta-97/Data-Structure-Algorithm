
'''Brute with 3 loops'''

''' Better Approach '''
def subarray_sum_k(nums,k):
    n=len(nums)
    count=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=nums[j]

            if sum==k:
                count+=1
    return count


nums=[1,1,1]
k=2
nums=[1,2,3]
k=3
nums=[1,2,3,-3,1,1,1,4,2,-3]
k=3
# print(subarray_sum_k(nums,k))


'''Optimal'''

def subarray_sum_k(nums,k):
    n=len(nums)
    count=0
    prefix_sum={}
    sum=0
    for i in range(n):
        prefix_sum[sum]=prefix_sum.get(sum,0)+1
        sum+=nums[i]

        if sum-k in prefix_sum:
            count+=prefix_sum.get(sum-k)
    return count


nums=[1,1,1]
k=2
nums=[1,2,3]
k=3
nums=[1,2,3,-3,1,1,1,4,2,-3]
# nums=[3,-3,1,1,1]
k=3
print(subarray_sum_k(nums,k))