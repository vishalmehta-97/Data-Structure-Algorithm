'''Brute Force'''
def searchMatrix(matrix,target):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==target:
                    return True
        return False

matrix=[
     [1,3,5,7],
     [10,11,16,20],
     [23,30,34,60]], 
target=3
# print(searchMatrix(matrix,target))

''' Optimal Approach '''    
'''Self'''

def searchMatrix(matrix,target):
    l=0
    h=len(matrix)-1
    while l<=h:
        m=(l+h)//2
        
        low=0
        high=len(matrix[0])-1
        while low<=high:
            mid=(low+high)//2

            if matrix[m][mid]==target:
                return True
            elif matrix[m][mid]>target:
                high=mid-1
            elif matrix[m][mid]<target:
                low=mid+1

        if high<0:
            h=m-1
        elif low>=len(matrix[0]):
            l=m+1
        else:
            return False
    return False


matrix=[
     [1,3,5,7],
     [10,11,16,20],
     [23,30,34,60]]
target=2
matrix=[[1,3,5,7],
        [10,11,16,20],
        [23,30,34,60]] 
target = 13
print(searchMatrix(matrix,target))