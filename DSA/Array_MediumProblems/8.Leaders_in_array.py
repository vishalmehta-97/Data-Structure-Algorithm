'''Brute Force'''

def leader(nums):
    n=len(nums)

    leaders=[]
    for i in range(n):
        leader=True
        for j in range(i+1,n):
            if nums[j]>nums[i]:
                leader=False
                break
        if leader==True:   
            leaders.append(nums[i])
    return leaders

nums=[1,2,5,3,1,2]
# print(leader(nums))

'''Optimal Solution'''

def leader_optimal(nums):
    n=len(nums)
    leader=[]
    # max=min(nums)
    max=-13324243243243242343243432
    for i in range(n-1,-1,-1):
        if nums[i]>max:
            leader.append(nums[i])
            max=nums[i]
    v=0
    j=len(leader)-1
    while v<j:
        leader[v],leader[j]=leader[j],leader[v]
        v+=1
        j-=1

    return leader

nums=[1,2,5,3,1,2]
nums=[-3,4,5,1,-4,-5]
print(leader_optimal(nums))