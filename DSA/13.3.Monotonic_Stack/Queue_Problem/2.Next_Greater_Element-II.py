''' Brute Force Approach '''

class Solution:
    def reCheck(self,nums,ii):
        for i in range(len(nums)):
            if i==ii:
                return -1

            if nums[ii]<nums[i]:
                return nums[i]
            
    def nextGreaterElements(self,nums):
        ans=[-1]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    ans[i]=nums[j]
                    break
            if ans[i]==-1:
                value=self.reCheck(nums,i) 
                ans[i]=value

        return ans


s=Solution()
nums=[2,10,12,1,11]
# print(s.nextGreaterElements(nums))

''' Better Brute Force Approach  (Using Imaginary Circular Array) '''

class Solution:
    def nextGreaterElements(self,nums):
        ans=[-1]*len(nums)
        for i in range(len(nums)):
            for j in range(i+1,i+len(nums)-1):
                j=j%len(nums)
                if nums[i]<nums[j]:
                    ans[i]=nums[j]
                    break
        return ans

s=Solution()
nums=[2,10,12,1,11]
# print(s.nextGreaterElements(nums))

''' Optimal Approach '''

class Solution:
    def nextGreaterElements(self,nums):
        stack=[]
        ans=[0]*len(nums)


        for i in range(2*len(nums)-1,-1,-1):
            if i>=len(nums):
                while stack and stack[-1]<=nums[i%len(nums)]:
                    stack.pop()
                stack.append(nums[i%len(nums)])
            else:
                while stack and stack[-1]<=nums[i]:
                    stack.pop()
                if not stack:
                    ans[i]=-1
                else:
                    ans[i]=stack[-1]

                stack.append(nums[i])   

        return ans

s=Solution()
nums=[2,10,12,1,11]
nums=[1,2,3,4,3]
nums=[1,2,1]
print(s.nextGreaterElements(nums))

''' After Trimming The code '''
 ## We can shorter the code by using the modular in the index of i which can help to avoid the duplicate lines in the conditions


class Solution:
    def nextGreaterElements(self,nums):
        stack=[]
        ans=[0]*len(nums)


        for i in range(2*len(nums)-1,-1,-1):
            while stack and stack[-1]<=nums[i%len(nums)]:
                stack.pop()
        
            if i<len(nums):
                if not stack:
                    ans[i]=-1
                else:
                    ans[i]=stack[-1]

            stack.append(nums[i%len(nums)])

        return ans

s=Solution()
nums=[2,10,12,1,11]
nums=[1,2,3,4,3]
nums=[1,2,1]
print(s.nextGreaterElements(nums))
