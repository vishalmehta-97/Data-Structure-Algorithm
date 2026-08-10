class Solution:
    def find(self,r_lenMax,c_lenMax,board,word,r,c,index,value):
        if index>=len(word):
            return True
        
        if r>=r_lenMax or c>=c_lenMax or c<0 or r<0:
            return False
    
        if board[r][c]!=word[index]:
            return False
        
        value=board[r][c]
        board[r][c]='$'  ## Changing the value of that index in the matrix to not go at that direction 
        top=self.find(r_lenMax,c_lenMax,board,word,r-1,c,index+1,value)
        left=self.find(r_lenMax,c_lenMax,board,word,r,c-1,index+1,value)
        down=self.find(r_lenMax,c_lenMax,board,word,r+1,c,index+1,value)
        right=self.find(r_lenMax,c_lenMax,board,word,r,c+1,index+1,value)
        board[r][c]=value
        if top or left or down or right:
            return True

        return False

    def exist(self,board,word):
        r_lenMax=len(board)
        c_lenMax=len(board[0])

        for r in range(len(board)):
            for c in range(len(board[0])):
                if word[0]==board[r][c]:
                    if self.find(r_lenMax,c_lenMax,board,word,r,c,0,value=board[r][c])==True:
                        return True
        
        return False
                    
s=Solution()
board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word="ABCB"
print(s.exist(board,word))
