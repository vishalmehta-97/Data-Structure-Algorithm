'''This Is Brute (O(n^3)) But it can be improved '''
def longestSubarray_Sum(arr,k):
    n=len(arr)
    max_length=0
    for i in range(n):
        for j in range(i,n+1):
            sum=0
            for l in range(i,j):
                sum+=arr[l]
            if sum==k:
                max_length=max(max_length,j-i)
    return max_length

arr=[1,2,3,1,1,4,1,1,1]
k=3
# print(longestSubarray_Sum(arr,k))


'''This Is improved Brute (O(n^2)) '''


def longestSubarray_Sumk(arr,k):
    n=len(arr)
    max_length=0
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum+=arr[j]
            if sum==k:
                max_length=max(max_length,j-i+1)
    return max_length

arr=[1,2,3,1,1,4,1,1,1]
k=3
print(longestSubarray_Sumk(arr,k))


def longestSubarray_sum_Hash(arr,k):
    prefix_sum=0
    max_length=0
    sum_index={0,-1}
    n=len(arr)

    for i in range(n):
        prefix_sum+=arr[i]


        if (prefix_sum-k) in sum_index:
            max_length=max(max_length,i-sum_index[prefix_sum-k])

    return max_length



arr=[1,2,3,1,1,4,1,1,1]
k=3
print(longestSubarray_sum_Hash(arr,k))

