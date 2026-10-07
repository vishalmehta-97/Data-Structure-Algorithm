class Solution:
    def nextSmallestElement(self,nums):
        ans=[0]*len(nums)
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1]>=nums[i]:
                stack.pop()

            if not stack:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(nums[i])

        return ans

s=Solution()
# nums=[4,8,5,2,25]
nums=[1,4,6,7,3,7,8,1]

print(s.nextSmallestElement(nums))


class Solution:
    def nextSmallestElement(self,nums):
        ans=[0]*len(nums)
        stack=[]
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1]<=nums[i]:
                stack.pop()

            if not stack:
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(nums[i])

        return ans

s=Solution()
# nums=[4,8,5,2,25]
nums=[1,4,6,7,3,7,8,1]

print(s.nextSmallestElement(nums))
