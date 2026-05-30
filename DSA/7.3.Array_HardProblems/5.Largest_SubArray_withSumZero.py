def largest_sub_brute(nums):
    n=len(nums)
    max_length=0
    
    for i in range(n):
        for j in range(i,n):
            total=0
            for k in range(i,j+1):
                total+=nums[k]
                length=0
            if total==0:
                length=k-i+1
                if length>max_length:
                    max_length=length
    return max_length


nums=[1,-1,3,2,-2,-8,1,7,10,23]
# nums=[15,-2,2,-8,1,7,10,23]
# nums=[6,-2,2,-8,1,7,4,-10]
# nums=[1, -1, 1, -1]
# nums=[9, -3, 3, -1, 6, -5]
# print(largest_sub_brute(nums))


def largest_sub_better(nums):
    n=len(nums)
    max_length=0
    
    for i in range(n):
        total=0
        for j in range(i,n):
            total+=nums[j]
            length=0
            if total==0:
                length=j-i+1
                if length>max_length:
                    max_length=length
    return max_length


nums=[1,-1,3,2,-2,-8,1,7,10,23]
# nums=[15,-2,2,-8,1,7,10,23]
# nums=[6,-2,2,-8,1,7,4,-10]
# nums=[1, -1, 1, -1]
# nums=[9, -3, 3, -1, 6, -5]
print(largest_sub_better(nums))


def Largest_sub_optimal(nums):
    n=len(nums)
    prefixSum={}
    sum=0
    max_length=0
    for i in range(n):
        length=0
        sum+=nums[i]
        if sum==0:
            max_length=i+1

        if sum in prefixSum:
            length=i-prefixSum.get(sum)
            if length >max_length:
                max_length=length

        if sum not in prefixSum :
            # prefixSum[sum]=prefixSum.get(sum,i)
            prefixSum[sum]=i    ## we can also do this
    return max_length


nums=[1,-1,3,2,-2,-8,1,7,10,23]
# nums=[15,-2,2,-8,1,7,10,23]
# nums=[6,-2,2,-8,1,7,4,-10]
# nums=[1, -1, 1, -1]
# nums=[9, -3, 3, -1, 6, -5]
print(Largest_sub_optimal(nums))