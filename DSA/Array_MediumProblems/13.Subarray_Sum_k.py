def subarraySum(nums,k):
    n=len(nums)
    count=0
    sum=0
    for i in range(n):
        for j in range(n):
            print(i,j)

nums=[1,2,3]
k=3
print(subarraySum(nums,k))