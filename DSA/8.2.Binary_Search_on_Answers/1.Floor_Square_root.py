''' Brute Force Approach '''

def floorsqrRoot(x):
    ans = 0
    for i in range(1, x + 1):
        if i * i <= x:
            ans = i
        else:
            break
    return ans

x=8
x=2147395599

print(floorsqrRoot(x))

'''Optimal Approach'''

def squareRoot(num):
    # nums=[i for i in range(num+1)]   ## Initially i did this using array but we can do without this
    # n=len(nums)
    low=0
    high=num
    ans=1
    
    while low<=high:
        mid=(low+high)//2  
        if mid**2<=num:
            ans=mid
            if ans*ans==num:
                return ans
            low=mid+1
        elif mid**2>num:
            high=mid-1
    return ans

num=4
num=2147395599
print(squareRoot(num))

def squareRoot_(num):    ## we can also do with this approach using the half search space and handling the starting cases with conditional statement
    if num<2:
        return num
    low=1
    high=num//2
    ans=1
    
    while low<=high:
        mid=(low+high)//2  
        if mid*mid<=num:
            ans=mid
            if ans*ans==num:
                return ans
            low=mid+1
        else:
            high=mid-1
    return ans

num=4
num=2147395599
print(squareRoot_(num))