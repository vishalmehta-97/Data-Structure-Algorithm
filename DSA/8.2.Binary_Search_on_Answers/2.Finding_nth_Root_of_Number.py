def nth_Root(n,m):
    low=1
    high=m
    eps=1e-6

    while (high-low)>eps:
        mid=(low+high)/2.0
        if mid**n<m:
            low=mid
        else:
            high=mid
    return high,low
        
n=4
m=69
print(nth_Root(n,m))

'''This is just a sligh different approach but same logic here i am using 
the differnt function to do the calculations because it help to avoid overflow 
which is a major issue in C++ not in python , we should use this method while doing
the Competative Programming
'''

def multiply(mid,n):
    ans=1
    for _ in range(1,n+1):
        ans=ans*mid
        if ans>m:
            return ans
    return ans

def nth_Root_(n,m):
    low=1
    high=m
    eps=1e-6

    while (high-low)>eps:
        mid=(low+high)/2.0
        if multiply(mid,n)<m:
            low=mid
        else:
            high=mid
    return high,low
        
n=4
m=81
print(nth_Root_(n,m))
