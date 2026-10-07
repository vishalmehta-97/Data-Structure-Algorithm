''' Brute Force Approach '''

class Solution:
    def celebrity(self, mat):
        knowMe=[0]*len(mat)
        iknow=[0]*len(mat)
       
        for i in range(len(mat)):
           for j in range(len(mat)):
               if mat[i][j]==1:
                   iknow[i]+=1
                   knowMe[j]+=1

        for i in range(len(iknow)):
           if iknow[i]==1:
               if knowMe[i]==len(mat):
                   return i
        return -1
    
s=Solution()
mat=[[1,1,0],
    [0,1,0],
    [0,1,1]]
# print(s.celebrity(mat))


''' Better Approach '''

class Solution:
    def celebrity(self, mat):
        for i in range(len(mat)):
           sum_row=0
           sum_clm=0
           for j in range(len(mat)):
               sum_row+=mat[i][j]
               sum_clm+=mat[j][i]

           if sum_row==1 and sum_clm==len(mat):
               return i

        return -1
    
s=Solution()
mat=[[1,1,0],
    [0,1,0],
    [0,1,1]]
# print(s.celebrity(mat))


''' Optimal Approach '''

class Solution:
    def celebrity(self, mat):
        top=0
        down=len(mat)-1

        while top<down:
            # if mat[top][down]==0 and mat[down][top]==1:
            #     down-=1
            # else:
            #     top+=1

            # for extra check
            if mat[top][down]==1:
                top+=1
            elif mat[down][top]==1:
                down-=1
            else:
                top+=1
                down-=1

        if top>down:   # this is related to the else condition
            return -1
            
        for i in range(len(mat)):
            if top!=i:
                if mat[top][i]!=0 or mat[i][top]!=1:
                    return -1
        return top

    
s=Solution()
mat=[[1,1,0],
    [0,1,0],
    [0,1,1]]
print(s.celebrity(mat))

5