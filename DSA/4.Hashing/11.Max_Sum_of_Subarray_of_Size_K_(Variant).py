'''Maximum Sum of Subarray of Size K (Variant)'''

# array=[2,1,5,1,3,2]
array=[1,1,5,3,2,5]
# array=[7,8,9,10,11,12]
def MaxSum(k):
    sum=0
    for i in range(0,k):
        sum+=array[i]

    maxS=sum
    start_index=0

    for i in range(k,len(array)):
        sum=sum-array[i-k]+array[i]
        
        if maxS<sum:
            start_index = i - k + 1
            maxS=sum

    print("Max Sum -->",maxS)
    return "index -->",start_index
 
print(MaxSum(3))
    