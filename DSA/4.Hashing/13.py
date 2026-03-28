array=[1,12,-5,-6,50,3]

def maxAverage(k):
    sum=0

    for i in range(0,k):
        sum+=array[i]
    maxS=sum

    for i in range(k,len(array)):
        sum=sum-array[i-k]+array[i]

        if sum>maxS:
            maxS=sum

    average=maxS/k
    return average

print(maxAverage(4))
