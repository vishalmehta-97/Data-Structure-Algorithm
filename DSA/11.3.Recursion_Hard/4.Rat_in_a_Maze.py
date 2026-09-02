class Solution:
    def ratGoing(self,grid,ansArray,path,row,clm):
        if row<0 or clm<0 or row==len(grid) or clm==len(grid):
            return

        if grid[row][clm]!=1:
            return

        if row==len(grid)-1 and clm==len(grid)-1:
            ansArray.append(path)
            return

        grid[row][clm]=-1

        # Down
        self.ratGoing(grid,ansArray,path+'D',row+1,clm)
        # Left
        self.ratGoing(grid,ansArray,path+'L',row,clm-1)
        # Right
        self.ratGoing(grid,ansArray,path+'R',row,clm+1)
        # Up
        self.ratGoing(grid,ansArray,path+'U',row-1,clm)

        grid[row][clm]=1

    def findPath(self, grid):
        ansArray=[]
        self.ratGoing(grid,ansArray,'',0,0)
        if len(ansArray)==0:
            return -1
        return ansArray


s=Solution()
n=4
grid=[
    [1,0,0,0],
    [1,1,0,1],
    [1,1,0,0],
    [0,1,1,1]
    ]
grid=[
    [1 ,0 ,0 ,0 ,0],
    [1, 1 ,0 ,1 ,1],
    [1, 1, 0 ,1 ,0],
    [0 ,0 ,0 ,0 ,1],
    [0, 1, 1 ,1 ,1]
]
print(s.findPath(grid))