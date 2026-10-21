class Solution:
    def sumCounts(self,nums):
        ans=0
        for i in range(len(nums)):
            s=set()
            for j in range(i,len(nums)):
                s.add(nums[j])
                ans+=len(s)*len(s)             
        return ans
s=Solution()
s=Solution()
nums=[1,2,1]
nums=[1,1]
print(s.sumCounts(nums))