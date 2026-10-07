''' Brute Force Approach '''

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        '''This is also a solution'''
        Ansarray=[]
        # i=0
        # while k<=len(nums):
        #     Ansarray.append(max(nums[i:k]))
        #     i+=1
        #     k+=1

        # return Ansarray

        ''' More Structured '''
        n=len(nums)
        for i in range(n-k+1):
            maxi=nums[i]
            for j in range(i,i+k):
                maxi=max(maxi,nums[j])
            Ansarray.append(maxi)

        return Ansarray
            

s=Solution()
nums=[1,3,-1,-3,5,3,6,7]
k=3
print(s.maxSlidingWindow(nums,k))

''' Optimal Approach '''

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        monotonicStack=deque()
        n=len(nums)
        ansArray=[]
        for i in range(n):
            while monotonicStack and nums[monotonicStack[-1]]<=nums[i]:
                monotonicStack.pop()

            if monotonicStack and monotonicStack[0]<=(i-k):
                monotonicStack.popleft()

            monotonicStack.append(i)

            if i>=(k-1):
                ansArray.append(nums[monotonicStack[0]])
                
        return ansArray
s=Solution()
nums=[1,3,-1,-3,5,3,6,7]
k=3
print(s.maxSlidingWindow(nums,k))