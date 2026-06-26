# '''Brute Force Approach'''

# def checkShip(weights,mid):
#     sum=weights[0]
#     count=1
#     for i in range(len(weights)):
#         sum+=weights[i]
#         if sum>mid:
#             count+=1
#             sum=weights[i]
#         else:
#             sum+=weights[i]

#     return count

# def shipwithDays(weights,days):
#     for i in range(max(weights),sum(weights)+1):
#         day=checkShip(weights,i)

#         if day<=days:
#             return i

# weights=[1,2,3,4,5,6,7,8,9,10]
# days=5
# print(shipwithDays(weights,days))


''' Optimal Approach '''

def checkShip(weights,mid,days):
    sum=weights[0]
    count=1
    for i in range(1,len(weights)):
        # sum+=weights[i]
        if (sum+weights[i])>mid:  ## here i did the addition
            count+=1
            sum=weights[i]
        else:
            sum+=weights[i]
    return count

def shipwithDays_(weights,days):
        '''
        We can also use this which can be optimal in some cases

        summ=0
        maxi=0
        for i in range(len(weights)):
            maxi=max(maxi,weights[i])
            summ+=weights[i]
            '''
        low=max(weights)
        high=sum(weights)

        ans=0
        while low<=high:
            mid=(low+high)//2
            if checkShip(weights,mid,days)<=days:
                ans=mid
                high=mid-1
            else:
                low=mid+1

        return ans

weights=[1,2,3,4,5,6,7,8,9,10]
weights=[10,50,100,100,50,100,100,100]
days=5
print(shipwithDays_(weights,days))
