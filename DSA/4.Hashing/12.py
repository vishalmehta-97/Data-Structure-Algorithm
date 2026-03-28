'''Minimum Sum Subarray of Size K'''

array=[2,1,5,1,3,2]

def minSum(k):
    sum=0
    for i in range(0,k):
        sum+=array[i]

    minS=sum
    start_index=0

    for i in range(k,len(array)):
        sum=sum-array[i-k]+array[i]
        
        if minS>sum:
            start_index = i - k + 1
            minS=sum

    print("Min Sum -->",minS)
    return start_index
 
print(minSum(3))
    