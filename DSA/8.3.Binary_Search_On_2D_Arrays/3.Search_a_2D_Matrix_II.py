''' Brute Force Approach '''
## Have done using Simple iteratiom in matrix


''' Better Approach '''
def searchMatrix(matrix,target):
    for i in range(len(matrix)):
        low=0
        high=len(matrix[0])-1
        while low<=high:
            mid=(low+high)//2

            if matrix[i][mid]==target:
                return True
            elif matrix[i][mid]>target:
                high=mid-1
            else:
                low=mid+1
    return False

''' Optimal Solution '''

def searchMatrix(matrix,target):
    row=0
    clm=len(matrix)-1
    while row<len(matrix) and clm>=0:
        if matrix[row][clm]==target:
            return True
        elif matrix[row][clm]>target:
            clm-=1
        else:
            row+=1
    return False
        
        
matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target=0
print(searchMatrix(matrix,target))