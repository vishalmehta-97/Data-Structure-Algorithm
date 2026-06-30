''' Brute Force Approach '''
def rowWithMax1s(arr):
    print(arr)
    ans=0
    index=-1
    for i in range(len(arr)):
        count=0
        for j in range(len(arr[0])):
            if arr[i][j]==1:
                count+=1
        if count>ans:
            ans=count
            index=i
        
    if ans==0:
        return -1
    else:
        return index
                

arr=[[1,1,1],
    [0,0,1],
    [0,0,0]]
arr=[[0,1,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [0,0,0,0]]
arr=[[0,0], 
    [0,0]]

# print(rowWithMax1s(arr))


''' Optimal Approach ''' 

def rowWithMax1s_(arr):
    max_sum=-1
    index=-1
    for i in range(len(arr)):
        low=0
        high=len(arr[0])-1
        while low<=high:
            mid=(low+high)//2
            if arr[i][mid]==0:
                low=mid+1
            else:
                high=mid-1
        sum=len(arr[0])-1-high
        if sum>max_sum:
            max_sum=sum
            index=i
    if index==0:
        return -1
    else:
        return index



arr=[[1,1,1],
    [0,0,1],
    [0,0,0]]
arr=[[0,0], 
    [0,0]]
arr=[[0,1,1,1],
    [0,0,1,1],
    [1,1,1,1],
    [0,0,0,0]]

print(rowWithMax1s_(arr))
