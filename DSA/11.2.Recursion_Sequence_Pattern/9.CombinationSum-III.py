class Solution:
    def generate(self,k,n,nums,ansArray,subseq,currSum,i):
        if currSum==n and k==0:
            ansArray.append(subseq.copy())
            return
        if currSum>n or k==0:
            return
        if i>=len(nums):
            return

        subseq.append(nums[i])
        self.generate(k-1,n,nums,ansArray,subseq,currSum+nums[i],i+1)
        subseq.pop()
        self.generate(k,n,nums,ansArray,subseq,currSum,i+1)

    def combinationSum3(self,k,n):
        ansArray=[]
        subseq=[]
        nums=[]
        for ele in range(1,9+1):
            nums.append(ele)
        i=0
        self.generate(k,n,nums,ansArray,subseq,0,i)
        return ansArray

# s=Solution() 
# k=9
# n=45
# print(s.combinationSum3(k,n))

''' More Optimal Approach '''

class Solution:
    def generate(self,k,n,nums,ansArray,subseq,i):
        if n==0 and k==0:
            ansArray.append(subseq.copy())
            return
        if n<0 or k==0:
            return
        if i>=len(nums):
            return
        if nums[i]>n:
            return
        

        subseq.append(nums[i])
        self.generate(k-1,n-nums[i],nums,ansArray,subseq,i+1)
        subseq.pop()
        self.generate(k,n,nums,ansArray,subseq,i+1)

    def combinationSum3(self,k,n):
        ansArray=[]
        subseq=[]
        nums=[]
        for ele in range(1,9+1):
            nums.append(ele)

        if (k*(k+1))//2>n:  ## Checking if the target is possible or not with that k no of elements
            return ansArray
        if sum(nums[-k:])<n:   ## Checking that the last k elements of the nums can form the target or not
            return ansArray
        
        i=0
        self.generate(k,n,nums,ansArray,subseq,i)
        return ansArray

s=Solution() 
k=3
n=9
print(s.combinationSum3(k,n))