from typing import List

''' Brute Force Approach'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        for i in range(len(heights)):
            mini=heights[i]
            for j in range(i,len(heights)):
                mini=min(mini,heights[j])
                maxArea=max(maxArea,mini*(j-i+1))

        return maxArea

s=Solution()
heights=[2,1,5,6,2,3]
heights=[2,4]
# print(s.largestRectangleArea(heights))


''' Brute Force Approach '''

class Solution:
    def prevSmaller_index(self,heights):
        stack=[]
        prevSmaller_indexx=[0]*len(heights)
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()

            if not stack:
                prevSmaller_indexx[i]=-1
            else:
                prevSmaller_indexx[i]=stack[-1]

            stack.append(i)

        return prevSmaller_indexx

    def nextSmaller_index(self,heights):
        stack=[]
        NextSmaller_indexx=[0]*len(heights)
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()

            if not stack:
                NextSmaller_indexx[i]=len(heights)
            else:
                NextSmaller_indexx[i]=stack[-1]

            stack.append(i)

        return NextSmaller_indexx
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        prevSmaller=self.prevSmaller_index(heights)
        nextSmaller=self.nextSmaller_index(heights)

        for i in range(len(heights)):
            maxArea=max((nextSmaller[i]-prevSmaller[i]-1)*heights[i],maxArea)

        return maxArea


s=Solution()
heights=[2,1,5,6,2,3]
heights=[2,4]
# print(s.largestRectangleArea(heights))


''' Optimal Approach '''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxArea=0
        for i in range(len(heights)):
            while stack and heights[stack[-1]]>=heights[i]:
                value=stack.pop()
                if stack:
                    prev=stack[-1]
                else:
                    prev=-1
                maxArea=max(maxArea,(i-prev-1)*heights[value])
            
            stack.append(i)

        while stack:
            value=stack.pop()
            print(value)
            if stack:
                prev=stack[-1]
            else:
                prev=-1
            maxArea=max(maxArea,(len(heights)-prev-1)*heights[value])

        return maxArea


s=Solution()
heights=[2,1,5,6,2,3]
heights=[3,2,10,11,5,10,6,3]
print(s.largestRectangleArea(heights))
