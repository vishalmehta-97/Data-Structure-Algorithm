'''Brute Approach'''

def setMatrixZero(matrix):
    n=len(matrix)
    matrixi=[]
    matrixj=[]
    for i in range(n):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                matrixi.append(i)
                matrixj.append(j)
    for v in range(len(matrixi)):
        for row in range(len(matrix[0])):
            matrix[matrixi[v]][row]=0

    for v in range(len(matrixj)):
        for clm in range(len(matrix)):
            matrix[clm][matrixj[v]]=0
    return matrix

matrix= [[1,1,1],[1,0,1],[1,1,1]]
matrix= [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# print(setMatrixZero(matrix))

'''One More Brute Force Approach'''
def mark_row(i,matrix):
    n=len(matrix)
    for v in range(len(matrix[0])):
        if matrix[i][v]!=0:
            matrix[i][v]=-1
    return matrix

def mark_clm(j,matrix):
    for v in range(len(matrix)):
        if matrix[v][j]!=0:
            matrix[v][j]=-1
    return matrix

def setMatrixZero(matrix):
    n=len(matrix)

    for i in range(n):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                mark_row(i,matrix)
                mark_clm(j,matrix)
    
    for i in range(n):
        for j in range(len(matrix[0])):
            if matrix[i][j]==-1:
                matrix[i][j]=0
    return matrix

matrix= [[1,1,1],[1,0,1],[1,1,1]]
matrix=[[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
matrix= [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# print(setMatrixZero(matrix))


'''Better Solution'''

def setMatrixZero(matrix):
    n=len(matrix)
    upper_row=[0]*len(matrix[0])
    index_clm=[0]*len(matrix)

    for i in range(n):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                upper_row[j]=1
                index_clm[i]=1   

    for i in range(n):
        for j in range(len(matrix[0])):
            if upper_row[j]==1 or index_clm[i]==1:
                matrix[i][j]=0
    return matrix
    
# matrix=[[1,1,1,1],[1,0,1,1],[1,1,0,1],[1,0,0,1]]
# matrix=[[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
matrix= [[1,1,1],[1,0,1],[1,1,1]]
matrix= [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# matrix= [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
# print(setMatrixZero(matrix))


'''Optimal Solution'''
def setMatrixZero_opt(matrix):
    n=len(matrix)
    clm=1
    for i in range(n):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                matrix[i][0]=0
                if j!=0:
                    matrix[0][j]=0
                else:
                    clm=0

    for i in range(n-1,0,-1):
        for j in range(len(matrix[0])-1,0,-1):
            if matrix[0][j]==0 or matrix[i][0]==0:
                matrix[i][j]=0
    if matrix[0][0]==0:
        for j in range(len(matrix[0])-1,-1,-1):
            if matrix[0][0]==0:
                matrix[0][j]=0
    if clm==0:
        for i in range(len(matrix)-1,-1,-1):
            if clm==0:
                matrix[i][0]=0

    return matrix

# matrix=[[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
# matrix= [[1,1,1],[1,0,1],[1,1,1]]
# matrix= [[1,1,1],[1,0,1],[1,1,1]]
# matrix= [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix= [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
print(setMatrixZero_opt(matrix))





'''This is From the leetcode itself'''

def setZeroes( matrix):
    rows = set()
    cols = set()
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                rows.add(r)
                cols.add(c)
    
    for r in rows:
        for c in range(len(matrix[0])):
            matrix[r][c] = 0
    
    for c in cols:
        for r in range(len(matrix)):
            matrix[r][c] = 0
    return matrix
matrix= [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
matrix= [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
print(setZeroes(matrix))