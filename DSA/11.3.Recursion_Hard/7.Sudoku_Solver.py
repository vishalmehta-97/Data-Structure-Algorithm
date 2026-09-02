class Solution:
    # def validPosition(self,board,i,r,c):
    #     for clm_ele in board[r]:
    #         if clm_ele==str(i):
    #             return False

    #     for row in range(len(board)):
    #         if board[row][c]==str(i):
    #             return False

    #     towhichRow=((r)//3)*3
    #     towhichClm=((c)//3)*3


    #     for row in range(towhichRow,towhichRow+3):
    #         for clm in range(towhichClm,towhichClm+3):
    #             if board[row][clm]==str(i):
    #                 return False
                
    #     return True

    def validPosition(self,board,i,r,c):
        for _ in range(0,len(board)):

            if board[r][_]==str(i):
                return False
            if board[_][c]==str(i):
                return False
            if board[3*(r//3)+(_//3)][3*(c//3)+(_%3)]==str(i):
                return False

        return True

            

    def checkEmptyPosition(self,board,rowtoStart):
        for r in range(rowtoStart,len(board)):
            for c in range(len(board[0])):
                if board[r][c]==".":
                    return r,c
        return -1,-1
                

    def completeSudoku(self,board,rowtoStart):
        r,c=self.checkEmptyPosition(board,rowtoStart)
        if r==-1 and c==-1:
            return True

        for i in range(1,len(board)+1):
            if self.validPosition(board,i,r,c):
                board[r][c]=str(i)
                rowtoStart=r
                if self.completeSudoku(board,rowtoStart):
                    return True
                board[r][c]="."

        return False
            

    def solveSudoku(self,board):
        self.completeSudoku(board,0)
        return board



s=Solution()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]
# print(s.solveSudoku(board))



'''More Optimal Approach'''

class Solution:
    def checkEmptyPosition(self,board,rowtoStart):
        for r in range(rowtoStart,len(board)):
            for c in range(len(board[0])):
                if board[r][c]==".":
                    return r,c
        return -1,-1
                

    def completeSudoku(self,board,rowtoStart,row_used,clm_used,box_used):
        r,c=self.checkEmptyPosition(board,rowtoStart)
        if r==-1 and c==-1:
            return True

        for i in range(1,len(board)+1):
            box=[(r//3)*3+(c//3)]
            if str(i) not in row_used[r] and str(i) not in clm_used[c] and str(i) not in box_used[(r // 3) * 3 + (c // 3)]:
                board[r][c]=str(i)
                row_used[r].add(str(i))
                clm_used[c].add(str(i))
                box_used[(r // 3) * 3 + (c // 3)].add(str(i))
                rowtoStart=r
                if self.completeSudoku(board,rowtoStart,row_used,clm_used,box_used):
                    return True
                board[r][c]="."
                row_used[r].remove(str(i))
                clm_used[c].remove(str(i))
                box_used[(r // 3) * 3 + (c // 3)].remove(str(i))


        return False
            

    def solveSudoku(self,board):
        ## Rows
        row_used=[set(board[x][:]) for x in range(len(board))]

        # Columns
        clm_used=[]
        for clm in range(len(board)):
            s=set()
            for i in range(len(board)):   
                s.add(board[i][clm])
            clm_used.append(s)

        # Box 9x9
        box_used = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    box = (r // 3) * 3 + (c // 3)
                    box_used[box].add(board[r][c])
        self.completeSudoku(board,0,row_used,clm_used,box_used)
        return board



s=Solution()
board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]


print(s.solveSudoku(board))