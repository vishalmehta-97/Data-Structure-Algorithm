from typing import List

''' Brute Force Approach '''

class Solution:
    def subnumsayRanges(self, nums: List[int]) -> int:
        total=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                total+=(max(nums[i:j+1])-min(nums[i:j+1]))
        return total
        

s=Solution()
nums=[1,2,3]
# print(s.subnumsayRanges(nums))


class Solution:
    def subnumsayRanges(self, nums: List[int]) -> int:
        total=0
        for i in range(len(nums)):
            mini=nums[i]
            maxi=nums[i]
            for j in range(i+1,len(nums)):
                mini=min(nums[j],mini)
                maxi=max(nums[j],maxi)
                total+=maxi-mini
        return total

s=Solution()
nums=[1,2,3]
nums=[1,4,3,2]
# print(s.subnumsayRanges(nums))



''' Optimal Approach '''

class Solution:
    def preMinimum(self,nums):
        stack=[]
        preMin_array=[0]*len(nums)
       
        for i in range(len(nums)):
            while stack and nums[stack[-1]]>nums[i]:
                stack.pop()

            if not stack:
                preMin_array[i]=-1
            else:
                preMin_array[i]=stack[-1]
            stack.append(i)

        return preMin_array

    def postMinimum(self,nums):
        stack=[]
        postMin_array=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):

            while stack and nums[stack[-1]]>=nums[i]:
                stack.pop()
            if not stack:
                postMin_array[i]=len(nums)
            else:
                postMin_array[i]=stack[-1]
            stack.append(i)
            
        return postMin_array
    
    ## Main Function 1
    def minimumMax_Sum(self,nums):
        preMini=self.preMinimum(nums)
        postMini=self.postMinimum(nums)

        total1=0
        for i in range(len(nums)):
            total1+=((postMini[i]-i)*(i-preMini[i]))*nums[i]

        return total1


    def preMaximum(self,nums):
        stack=[]
        preMax_array=[0]*len(nums)

        for i in range(len(nums)):
            while stack and nums[stack[-1]]<nums[i]:
                stack.pop()
            if not stack:
                preMax_array[i]=-1
            else:
                preMax_array[i]=stack[-1]
            stack.append(i)

        return preMax_array
    
    def postMaximum(self,nums):
        stack=[]
        postMax_array=[0]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            while stack and nums[stack[-1]]<=nums[i]:
                stack.pop()
            if not stack:
                postMax_array[i]=len(nums)
            else:
                postMax_array[i]=stack[-1]
            stack.append(i)

        return postMax_array
    

    ## Main Function 2
    def maximumMax_Sum(self,nums):
        preMaxi=self.preMaximum(nums)
        postMaxi=self.postMaximum(nums)
        total2=0
        for i in range(len(nums)):
            total2+=((i-preMaxi[i])*(postMaxi[i]-i))*nums[i]

        return total2
            
    def subnumsayRanges(self, nums: List[int]) -> int:
        maximumSum=self.maximumMax_Sum(nums)
        minimumSum=self.minimumMax_Sum(nums)
        total=maximumSum-minimumSum
        return total


s=Solution()
nums=[1,4,3,2]
nums=[1,3,3]
nums=[4,-2,-3,4,1]
print(s.subnumsayRanges(nums))
