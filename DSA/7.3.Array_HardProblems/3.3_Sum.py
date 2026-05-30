''' Brute Force Approach'''

def Tsum(nums):
    n=len(nums)
    output=[]
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    ans=[]
                    ans.append(nums[i])
                    ans.append(nums[j])
                    ans.append(nums[k])
                    ans.sort()
                    if ans not in output:
                        output.append(ans)

    return output
                    
nums=[0,1,1]
nums=[-1,0,1,2,-1,-4]
nums=[0,0,0]
# print(Tsum(nums))

'''Better Approach'''
# We have used the sets instead of basic hasharray so that we do the lookups very fast and does not store the duplicate answers

def T_Sum(nums):
    n=len(nums)
    output=set()
    for i in range(n):
        hash=set()
        for j in range(i+1,n):
            sum=nums[i]+nums[j]
            if -(sum) in hash:
                ans=[nums[i],nums[j],-sum]
                ans.sort()

                output.add(tuple(ans))
            hash.add(nums[j])
            
    return [list(i) for i in output]


nums=[-1,0,1,2,-1,-4]
# nums=[0,1,1]
# nums=[0,0,0]
# print(T_Sum(nums))


def T_sum_Opt(nums):
    nums.sort()
    n=len(nums)
    i=0
    output=[]
    while i<n:
        j=i+1
        k=n-1
        while j<k:
            total=nums[i]+nums[j]+nums[k]
            if total==0:
                answer=[]
                answer.append(nums[i])
                answer.append(nums[j])
                answer.append(nums[k])
                j+=1
                k-=1
                while j<k and nums[j]==nums[j-1]:
                    j+=1
                while j<k and nums[k]==nums[k+1]:
                    k-=1
                output.append(answer)
            elif total<0:
                j+=1
            elif total>0:
                k-=1
        i+=1
        while i<n and nums[i]==nums[i-1]:
            i+=1
    return output
nums=[-2,-2,-2,-1,-1,-1,0,0,0,2,2,2,2]
nums=[-1,0,1,2,-1,-4]
nums=[0,0,0]
nums=[0,1,1]
print(T_sum_Opt(nums))