'''The Brute One (This Approach is to find the any no in Pascal's Triangle using the Row and Column Number using Combination Formula (nCr))'''

def pascalTri(row,clm):
    row-=1
    clm-=1
    up=1

    for i in range(clm):
        up*=row-i
        up=up//(i+1)

    return up
    

# print(pascalTri(3,2))


'''Using the Same formula we'll try the second approach where we have to print the Full nth Row of the Pascal's Triangle'''

def pascalTri_sec(row):
    list=[]
    row-=1
    up=1
    clm=row
    while clm>=0:
        for i in range(clm):
            up*=row-i
            up=up//(i+1)
        list.append(up)
        up=1
        clm-=1

    return list

# print(pascalTri(5))

''' Second Approach with Optimal Solution '''

def pascalTri_secOptimal(row):
    row+=1
    clm=row
    ans=1
    print(ans,end=" ")
    for i in range(1,clm):
        ans=ans*(row-i)
        ans=ans//i

        print(ans,end=" ")

# pascalTri_secOptimal(4)


''' Third Approach is where we have to print the whole Pascal's Triangle '''

'''Optimal but my approach'''
def pascalTri_(row):

    answer=[]
    for i in range(1,row+1):
        row_list=[1]
        ans=1
        for j in range(1,i):
            ans=ans*(i-j)
            ans=ans//j
            row_list.append(ans)
        # print(row_list)
        answer.append(row_list)
    return answer
    
pascalTri_(5)


'''Optimal but trying to code more clean using functions'''

def generate_clms(n):
    n+=1
    ans_row=[1]
    ans=1
    for i in range(1,n):
        ans=ans*(n-i)
        ans=ans//i
        ans_row.append(ans)
    return ans_row

def pascalTri(n):
    answer=[]
    for i in range(1,n+1):
        sol=generate_clms(i)
        answer.append(sol)
    return answer
print(pascalTri(5))

