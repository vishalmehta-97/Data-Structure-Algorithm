'''This is the better solution and there is one brute force approach where we do the things with 3 loops'''

def maximum_subarray(arr):
    n=len(arr)
    total_sum=arr[0]
    for i in range(n):
        sum=0
        for j in range(i,n):
            sum=sum+arr[j]
            if sum>total_sum:
                total_sum=sum

    return total_sum

arr=[-2,1,-3,4,-1,2,1,-5,4]
arr=[-1,0,-2]
# print(maximum_subarray(arr))


'''Optimal Approach ( Kadane's Algorithm )'''

def maximum_subarray_Optimal(arr):
    sum=0
    max=min(arr)
    n=len(arr)

    for i in range(n):
        if sum==0:
            start=i
        sum+=arr[i]
        if sum>max:
            max=sum
            ansStart=start
            ansEnd=i+1
        
        if sum<0:
            sum=0
    print("SubArray",arr[ansStart:ansEnd])
    return max


arr=[-2,1,-3,4,-1,2,1,-5,4]
arr=[-1,0,-2]
arr=[-2,-3,4,-1,-2,1,5,-3]
arr=[-1, 2, 3, -1, 2, -6, 5]
print(maximum_subarray_Optimal(arr))