'''This One is Brute Force'''
def rotateLeft(nums,k):
    temp=nums[:k]
    n=len(nums)
    for i in range(k,n):
        nums[i-k]=nums[i]
    
    nums[n-k:n]= temp[:]
    return nums

nums=[1,2,3,4,5,6,7]
k=2
print(rotateLeft(nums,k))



'''This One is Optimal'''
def rotateLeft(nums,k):
    n=len(nums)
    reverse(nums,0,k-1)
    reverse(nums,k,n-1)
    reverse(nums,0,n-1)
    return nums

def reverse(nums,i,j):
    while i<=j:
        nums[i],nums[j]=nums[j],nums[i]
        i+=1
        j-=1
    return nums


nums=[11,20,32,48,25,61,17]
k=3
n=len(nums)
print(rotateLeft(nums,k))