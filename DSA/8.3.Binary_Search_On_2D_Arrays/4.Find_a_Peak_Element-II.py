'''Brute Force'''
def find_Peak_Element_(mat):
    pass

mat=[[1,4],[3,2]]
# print(find_Peak_Element_(mat))

''' Better Approach '''

def find_Peak_Element(mat):
    max=float('-inf')
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]>max:
                max=mat[i][j]
                x=i
                y=j
    return [x,y]


mat=[[1,4],[3,2]]
# print(find_Peak_Element(mat))


''' Optimal Approach '''
def give_me_the_max(mat,mid):
    max=float('-inf')
    for i in range(len(mat)):
        if mat[i][mid]>max:
            max=mat[i][mid]
            index=i
    return max,index


def find_Peak_Element_(mat):
    ## we can perform this question by taking low and high in row also

    low=0
    high=len(mat[0])-1
    while low<=high:
        mid=(low+high)//2

        max,index=give_me_the_max(mat,mid)

        ## Left for Certain Conditions
        if mid==0:
            left=-1
        else:
            left=mat[index][mid-1]

        if mid==len(mat[0])-1:
            right=-1
        else:
            right=mat[index][mid+1]

        if max>left and max>right:
            return [index,mid]
        elif max<left:
            high=mid-1
        else:
            low=mid+1
    
    return -1


mat=[[1,4],[3,2]]
# mat =[
#     [4, 2, 5, 1, 4, 5],
#     [2, 9, 3, 2, 3, 2],
#     [1, 7, 6, 0, 1, 3],
#     [3, 6, 2, 3, 7, 2]
# ]
print(find_Peak_Element_(mat))

