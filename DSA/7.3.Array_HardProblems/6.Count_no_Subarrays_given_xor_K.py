'''Count Number of Subarray with given xor K'''


'''This is Better Solution we can do brute with the help of 3 loops'''

def subarrayXOR(nums,k):
    n=len(nums)
    count=0
    for i in range(n):
        xor=0
        for j in range(i,n):
            xor^=nums[j]

            if xor==k:
                count+=1

    return count
     
nums=[4,2,2,6,4]
k=6
# print(subarrayXOR(nums,k))


'''Optimal Solution'''

def subarrayXOR(nums,k):
    n=len(nums)
    count=0
    xor=0
    frontXOR={}
    for i in range(n):
        frontXOR[xor]=frontXOR.get(xor,0)+1
        xor^=nums[i]
        x=xor^k
        if x in frontXOR:
            count+=frontXOR.get(x)
    return count

     
nums=[4,2,2,6,4]
k=6
print(subarrayXOR(nums,k))
