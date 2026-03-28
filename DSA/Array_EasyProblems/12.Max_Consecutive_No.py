def max_Consecutive(array):
    max_no=0
    count=0
    n=len(array)
    for i in range(n):
        if array[i]==1:
            count+=1
            max_no=max(count,max_no)
        else:
            count=0
    return max_no

array=[1,1,0,1,1,1]
print(max_Consecutive(array))