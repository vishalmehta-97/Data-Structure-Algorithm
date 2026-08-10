'''Optimal Approach'''

'''We can optimize this ques approach by Checking the safe place using Bit Manipulation or Hash Sets
From O(N) to O(1) So here is the Approach Using Hash Sets'''

class Solution:
    def checkPositiontoPlace(self,n,ansArray,subAnsArray,row,cStet,Rset,Lset):
        if row>=n:
            ansArray.append(subAnsArray.copy())     
            return ansArray
        
        for clm in range(n):
            if (clm not in cStet) and ((row+clm) not in Rset) and ((row-clm) not in Lset):
                cStet.add(clm)
                Rset.add(row+clm)
                Lset.add(row-clm)

                subAnsArray[row] = (subAnsArray[row][:clm] +'Q'+subAnsArray[row][clm+1:])

                self.checkPositiontoPlace(n,ansArray,subAnsArray,row+1,cStet,Rset,Lset)

                cStet.discard(clm)
                Rset.discard(row+clm)
                Lset.discard(row-clm)
        
                subAnsArray[row] = (subAnsArray[row][:clm] +'.'+subAnsArray[row][clm+1:])

    def solveNQueens(self,n):
        ansArray=[]
        subAnsArray=[]
        for _ in range(n): 
            subAnsArray.append(n*".")

        ClmSet=set()
        RightDiagonalSet=set()
        LeftDiagonalSet=set()

        self.checkPositiontoPlace(n,ansArray,subAnsArray,0,ClmSet,RightDiagonalSet,LeftDiagonalSet)
        return ansArray

s=Solution()
print(s.solveNQueens(n=4))


'''Normal Approach'''

class Solution:
    def checkifSafe(self,subAnsArray,r,c):
        for i in range(r-1,-1,-1):
            if subAnsArray[i][c]=="Q":
                return False
            
        ## Check Left Diagonals
        row=r-1
        clm=c-1
        while row>=0 and clm>=0:
            if subAnsArray[row][clm]=='Q':
                return False
            row-=1
            clm-=1
            
        ## Check Right Diagonals
        row=r-1
        clm=c+1
        while row>=0 and clm<len(subAnsArray):
            if subAnsArray[row][clm]=='Q':
                return False
            row-=1
            clm+=1

        return True

    def checkPositiontoPlace(self,n,ansArray,subAnsArray,row):
        if row>=n:
            # ansArray.append(subAnsArray.copy())     
            ''' We can do this here because it will gonna copy the outside matrix board where there were no Queen '''
            ansArray.append(["".join(row) for row in subAnsArray])   ## We used join here to make that into a sperate String required in leetcode
            return ansArray
        
        for clm in range(n):
            if self.checkifSafe(subAnsArray,row,clm):
                subAnsArray[row][clm]='Q'
                self.checkPositiontoPlace(n,ansArray,subAnsArray,row+1)
                subAnsArray[row][clm]='.'

    def solveNQueens(self,n):
        ansArray=[]
        subAnsArray=[]
        for _ in range(n): 
            subAnsArray.append(n*["."]) # Making of board 
            '''In here we have made a separate array instead of the whole string so we have to do changes in last while adding in the ansArray so that we can make the output in String Format'''

        self.checkPositiontoPlace(n,ansArray,subAnsArray,0)
        return ansArray

s=Solution()
print(s.solveNQueens(n=4))


''' Same Same but just Output Formatting Apporach'''


class Solution:
    def checkifSafe(self,subAnsArray,r,c):
        for i in range(r-1,-1,-1):
            if subAnsArray[i][c]=="Q":
                return False
            
        ## Check Left Diagonals
        row=r-1
        clm=c-1
        while row>=0 and clm>=0:
            if subAnsArray[row][clm]=='Q':
                return False
            row-=1
            clm-=1
            
        ## Check Right Diagonals
        row=r-1
        clm=c+1
        while row>=0 and clm<len(subAnsArray):
            if subAnsArray[row][clm]=='Q':
                return False
            row-=1
            clm+=1

        return True

    def checkPositiontoPlace(self,n,ansArray,subAnsArray,row):
        if row>=n:
            ansArray.append(subAnsArray.copy())     
            return ansArray
        
        for clm in range(n):
            if self.checkifSafe(subAnsArray,row,clm):
                subAnsArray[row] = (subAnsArray[row][:clm] +'Q'+subAnsArray[row][clm+1:])   ## Here we have Concatinated the String Because string is Imutable and we can change it like Array or others
                self.checkPositiontoPlace(n,ansArray,subAnsArray,row+1)
                subAnsArray[row] = (subAnsArray[row][:clm] +'.'+subAnsArray[row][clm+1:])

    def solveNQueens(self,n):
        ansArray=[]
        subAnsArray=[]
        for _ in range(n): 
            subAnsArray.append(n*".")

        self.checkPositiontoPlace(n,ansArray,subAnsArray,0)
        return ansArray

s=Solution()
print(s.solveNQueens(n=4))


