
# '''Brute Force'''

def rotate_matrix(matrix):
    n=len(matrix)
    rotated = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1]=matrix[i][j]
        
    return rotated
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
# print(rotate_matrix(matrix))

# '''Optimal'''
def rotate_matrix_optimal(matrix):
    n=len(matrix)
    matrix=[list(row) for row in zip(*matrix)]

    for i in range(n):
        for j in range(n):
            matrix[i][j]=matrix[i][j]
    print(matrix)

    for k in range(n):
        i=0
        j=n-1
        while i<=j:
            matrix[k][i],matrix[k][j]=matrix[k][j],matrix[k][i]
            i+=1
            j-=1
    return matrix

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

# print(rotate_matrix_optimal(matrix))


def rotateMatrix(matrix):
    n=len(matrix)
    mat=[[0]*n for _ in range(len(matrix))]

    for i in range(n):
        for j in range(n):
            mat[j][n-1-i]=matrix[i][j]
    print(mat)


matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
# print(rotateMatrix(matrix))


def rotateMatrix_optimal(matrix):
    n=len(matrix)

    for i in range(n-1):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

    for k in range(n):
        i=0
        j=n-1

        while i<j:
            matrix[k][i],matrix[k][j]=matrix[k][j],matrix[k][i]
            i+=1
            j-=1
    return matrix
            
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print(rotateMatrix_optimal(matrix))
