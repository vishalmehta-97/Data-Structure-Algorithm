''' Brute Force (PowerSet Approach (Using Bit Manipluation)) Approach '''

class Solution:
    def subsetSums(self,nums):
        n=len(nums)
        arraySum=[]
        for num in range(1<<n):
            subseqSum=0
            for i in range(n):
                if num & (1<<i):
                    subseqSum+=nums[i]
            arraySum.append(subseqSum)

        return arraySum

s=Solution()
# nums=[2,3]
nums=[1,2,1]
print(s.subsetSums(nums))
        

''' Optimal Approach '''

class Solution:
    def generate(self,nums,array,total_sum,i):
        if i>=len(nums):
            array.append(total_sum)
            return
        total_sum+=nums[i]
        self.generate(nums,array,total_sum,i+1)
        total_sum-=nums[i]
        self.generate(nums,array,total_sum,i+1)

    def subsetSums(self,nums):
        array=[]
        total_sum=0
        self.generate(nums,array,total_sum,0)
        return array
    
s=Solution()
nums=[2,3]
nums=[1,2,1]
print(s.subsetSums(nums))
        