from typing import List

''' Brute Force Approach '''

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        prefixmax=[]
        suffixmax=[0]*n
        for i in range(n):   ## Calculating PrefixMax and SuffixMax for each height[i] so we can calculate the trap water by getting the value of leftmax and rightmax of that perticular value
            if i==0:
                smax=height[n-1]
                pmax=height[0]
                suffixmax[n-1]=smax
                prefixmax.append(pmax)
            else:
                smax=max(smax,height[n-1-i])
                pmax=max(pmax,height[i])
                prefixmax.append(pmax)
                suffixmax[len(height)-1-i]=smax


        totalwater=0
        for i in range(len(height)):
            leftmax=prefixmax[i]
            rightmax=suffixmax[i]

            if leftmax>height[i] and rightmax>height[i]:
                totalwater+=min(leftmax,rightmax)-height[i]

        return totalwater

s=Solution()
height=[0,1,0,2,1,0,1,3,2,1,2,1]
# print(s.trap(height))


''' Slightly Better Approach than Brute Force '''

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        suffixmax=[0]*n
        for i in range(n-1,-1,-1):   ## instead of calculating both suffix and prefix we will compute only suffixMax and we'll handle the prefixMax in the second loop in each step by calculating
            if i==n-1:
                suffmax=height[i]
                suffixmax[n-1]=suffmax
            else:
                suffmax=max(height[i],suffmax)
                suffixmax[i]=suffmax

        totalwater=0
        prefixMax=float('-inf')
        for i in range(len(height)):
            prefixMax=max(prefixMax,height[i])
            rightmax=suffixmax[i]

            if prefixMax>height[i] and rightmax>height[i]:
                totalwater+=min(prefixMax,rightmax)-height[i]


        return totalwater

s=Solution()
height=[0,1,0,2,1,0,1,3,2,1,2,1]
# print(s.trap(height))


''' Optimal Approach '''

class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        leftmax=0
        rightmax=0
        total=0
        l=0
        r=n-1

        while l<r:
            leftmax=max(leftmax,height[l])
            rightmax=max(rightmax,height[r])

            if rightmax>leftmax:
                total+=leftmax-height[l]
                l+=1
            else:
                total+=rightmax-height[r]
                r-=1

        return total


s=Solution()
height=[0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(height))