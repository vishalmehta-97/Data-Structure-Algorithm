# Maximum Sum subarray of size k
array=[2,1,5,1,3,2]
def MaxSum(k):
    sum=0
    maxsum=0
    l=0
    r=k
    for i in range(l,r):
        sum+=array[i]
    maxsum=sum
    
    for i in range(k, len(array)):
        sum=sum-array[i-k]+array[i]

        if sum>maxsum:
            maxsum=sum

    return maxsum    
    
print(MaxSum(3))

'''Short and Good Code For This Question'''

# array = [2,1,5,1,3,2]

# def MaxSum(k):
#     sum = 0
#     maxsum = 0

#     for i in range(len(array)):
#         sum += array[i]

#         # shrink window if size > k
#         if i >= k:
#             sum -= array[i-k]

#         # when window size == k
#         if i >= k-1:
#             maxsum = max(maxsum, sum)

#     return maxsum

# print(MaxSum(3))

    
