''' Brute Force Approach '''
def matrix_median(matrix):
    sorted_array=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sorted_array.append(matrix[i][j])

    sorted_array.sort()
    print(sorted_array)

    return sorted_array[len(sorted_array)//2]


matrix=[
    [1,5,7,9,11],
    [2,3,4,5,10],
    [9,10,12,14,16]
    ]
matrix=[[37,41, 48, 49, 51],
[4 ,9 ,10 ,16 ,22],
[28 ,34 ,36, 37, 38],
[18 ,20 ,28 ,32 ,38],
[15 ,17, 21 ,23 ,27]]

# print(matrix_median(matrix))

''' Better Approach '''

# def check_Digit(matrix,mid):
#     count=0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if matrix[i][j]<=mid:
#                 count+=1

#     return count


## Instead of this whole function we can use the python count module also
import bisect
def check_Digit(matrix,mid):     
    count=0
    for row in matrix:
        count+=bisect.bisect(row, mid)
    return count
''' We can also use Binary Search to get the Count '''    

def matrix_median_(matrix):

    # low=min(map(min,matrix))
    # high=max(map(max,matrix))  ## this is to get the max and min in the matrix but more Time
    low=min(row[0] for row in matrix)
    high=max(row[-1] for row in matrix)   ## this is more optimal way to get the low and high because the rows are in sorted order 

    n=len(matrix)*len(matrix[0])  ## (n x m)

    while low<=high:
        mid=(low+high)//2

        count=check_Digit(matrix,mid)
        if count<=n//2:
            low=mid+1
        else:
            high=mid-1

    return low

matrix=[
    [1,5,7,9,11],
    [2,3,4,5,10],
    [9,10,12,14,16]
    ]
matrix=[[37,41,48,49,51],
[4,9,10,16,22],
[28,34,36,37,38],
[18,20,28,32,38],
[15,17,21,23,27]]

print(matrix_median_(matrix))