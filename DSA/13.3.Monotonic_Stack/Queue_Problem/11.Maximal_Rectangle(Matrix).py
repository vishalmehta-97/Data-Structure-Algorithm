class Solution:
    def areaOfRectangle(self,rectangle_Array):
        maxArea=0
        stack=[]
        for i in range(len(rectangle_Array)):
            while stack and rectangle_Array[stack[-1]]>=rectangle_Array[i]:
                value=stack.pop()
                if not stack:
                    prev=-1
                else:
                    prev=stack[-1]
                maxArea=max(maxArea,(i-prev-1)*rectangle_Array[value])
            stack.append(i)

        while stack:
            value=stack.pop()

            if not stack:
                prev=-1
            else:
                prev=stack[-1]

            maxArea=max(maxArea,(len(rectangle_Array)-prev-1)*rectangle_Array[value])
        return maxArea

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        maxAreaRectangle=0
        rectangles=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=="1":
                    rectangles[j]+=1
                else:
                    rectangles[j]=0

            maxAreaRectangle=max(maxAreaRectangle,self.areaOfRectangle(rectangles))

        return maxAreaRectangle
                

s=Solution()
matrix=[["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]]
print(s.maximalRectangle(matrix))