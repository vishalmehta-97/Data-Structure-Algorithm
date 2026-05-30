'''Brute Force Approach'''
def missandrepeat_brute(nums):
    n=len(nums)
    output=[]
    missing=-1
    repeat=-1
    for i in range(1,n+1):
        count=0
        for j in range(n):
            if i==nums[j]:
                count+=1
            
        if count>1:
            repeat=i
        if count==0:
            missing=i

        if missing!=-1 and repeat!=-1:
            break

    output.append(repeat)
    output.append(missing)

    return output

nums=[4,3,6,2,1,1]
# nums=[3,5,4,1,1]
nums=[1,2,3,6,7,5,7]
# print(missandrepeat_brute(nums))


'''Better Approach'''
def missing_Repeating(nums):
    n=len(nums)
    hash=[0]*(n+1)

    for i in nums:
        hash[i]+=1
    miss=-1
    repeat=-1
    for i in range(1,len(hash)):
        if hash[i]>1:
            repeat=i
        if hash[i]==0:
            miss=i
        if miss!=-1 and repeat!=-1:
            break

    return [repeat,miss]
        
        

    
nums=[4,3,6,2,1,1]
# nums=[3,5,4,1,1]
nums=[1,2,3,6,7,5,7]
# print(missing_Repeating(nums))


'''Optimal Approach'''

def missing_Repeating(nums):
    n=len(nums)
    sum=0
    squares=0
    for i in range(n):
        sum+=nums[i]
        squares+=nums[i]**2
    print(sum)
    print(squares)

    sumOfN=(n*(n+1))//2
    squaresOfN=(n*(n+1)*(2*n+1))//6
    print(sumOfN)
    print(squaresOfN)
    ## We have done this using Equation like x-y and x+y like this
    val1=sum-sumOfN   ## x-y
    val2=squares-squaresOfN

    val2=val2//val1  ## x+y

    x=0
    x=(val1+val2)//2   # x=(x+y+x-y)/2
    y=val2-x   # y=x+y-x

    return [x,y]

nums=[4,3,6,2,1,1]
print(missing_Repeating(nums))


''' One More Optimal Approach (XOR Method)'''