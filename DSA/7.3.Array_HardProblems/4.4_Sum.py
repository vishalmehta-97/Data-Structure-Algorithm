'''Brute Force'''
def f_Sum(nums,target):
    n=len(nums)
    output=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    answer=[]
                    sum=nums[i]+nums[j]+nums[k]+nums[l]
                    if sum==target:
                        answer.append(nums[i])
                        answer.append(nums[j])
                        answer.append(nums[k])
                        answer.append(nums[l])
                        answer.sort()
                        if answer not in output:
                            output.append(answer)
    return output

# nums=[1,0,-1,0,-2,2]
# target=0
# nums=[2,2,2,2,2]
# target=8
# print(f_Sum(nums,target))


'''Better Approach'''

def F_sum(nums,target):
    n=len(nums)
    output=set()
    for i in range(n):
        for j in range(i+1,n):
            hash=set()
            for k in range(j+1,n):
                sum=nums[i]+nums[j]+nums[k]
                forth=target-sum
                if forth in hash:
                    answer=tuple(sorted([nums[i],nums[j],nums[k],forth]))   ## We use tuple because set can only store fixed (immutable) values, and list can change.(means we can't store list in set)
                    output.add(answer)
                hash.add(nums[k])

    return [list(i) for i in output]

# nums=[1,0,-1,0,-2,2]
# target=0
# nums=[2,2,2,2,2]
# target=8
nums=[-3,-1,0,2,4,5]
target=1
# print(F_sum(nums,target))


def F_sum_Opt(nums,target):
    nums.sort()
    n=len(nums)
    output=[]
    i=0

    while i<n:
        j=i+1
        while j<n:
            k=j+1
            l=n-1
            while k<l:
                sum=nums[i]+nums[j]+nums[k]+nums[l]
                answer=[]
                if sum==target:
                    answer.append(nums[i])
                    answer.append(nums[j])
                    answer.append(nums[k])
                    answer.append(nums[l])
                
                    output.append(answer)
                    k+=1
                    l-=1
                    while k<l and nums[k]==nums[k-1]:
                        k+=1
                    while k<l and nums[l]==nums[l+1]:
                        l-=1

                elif target>sum:
                    k+=1

                elif target<sum:
                    l-=1
            j+=1
            while j<n and nums[j]==nums[j-1]:
                j+=1
        i+=1
        while i<n and nums[i]==nums[i-1]:
            i+=1

    return output

nums=[1,1,1,2,2,2,3,3,3,4,4,4,5,5]
target=8
print(F_sum_Opt(nums,target))
