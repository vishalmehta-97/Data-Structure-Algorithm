def optimalSpiral(matrix):
    m=len(matrix)
    n=len(matrix[0])
    top=0
    bottom=m-1
    right=n-1
    left=0
    answer=[]
    # while matrix[top][left]!=matrix[bottom][right]:
    while top<=bottom and left<=right:
        for i in range(left,right+1):
            print(matrix[top][i])
            a=matrix[top][i]
            answer.append(a)
        top+=1

        for i in range(top,bottom+1):
            print(matrix[i][right])
            b=matrix[i][right]
            answer.append(b)
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                print(matrix[bottom][i])
                c=matrix[bottom][i]
                answer.append(c)
            bottom-=1

            # if top==bottom:
            #     for i in range(left,right+1):
            #         print("mat",matrix[top][i])
            #         d=matrix[top][i]
            #         answer.append(d)
            #     return answer
                    
        if left<=right:
            for i in range(bottom,top-1,-1):
                print(matrix[i][left])
                d=matrix[i][left]
                answer.append(d)
            left+=1 

    return answer
    
    
    




# matrix=[
#     [1,2,3,4,5,6],
#     [20,21,22,23,24,7],
#     [19,32,33,34,25,8],
#     [18,31,36,35,26,9],
#     [17,30,29,28,27,10],
#     [16,15,14,13,12,11]
#     ]

matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
        ]
print(optimalSpiral(matrix))