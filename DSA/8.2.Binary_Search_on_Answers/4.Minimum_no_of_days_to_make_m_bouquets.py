'''Brute Force Approach'''

def minDays_Bloom(bloomDay,m,k):
    maxi=max(bloomDay)
    mini=min(bloomDay)

    n=len(bloomDay)
    if m*k>n:
        return -1
    for i in range(mini,maxi+1):
        boque=0
        count=0
        for ele in range(n):
            if bloomDay[ele]<=i:
                count+=1
            elif bloomDay[ele]>i:
                boque+=count//k
                count=0
        boque+=count//k

    
        if boque>=m:
            return i

bloomDay=[1,10,3,10,2]
m=3
k=1
bloomDay=[7,7,7,7,13,11,12,7,7]
m=2
k=3
bloomDay=[1000000000,1000000000]
m=1
k=1
print(minDays_Bloom(bloomDay,m,k))


'''Optimal Approach'''
def check(bloomDay,mid,k):
    count=0
    boque=0
    for i in range(len(bloomDay)):
        if bloomDay[i]<=mid:
            count+=1
        elif bloomDay[i]>mid:
            boque+=count//k
            count=0
    boque+=count//k
    return boque

def minDays(bloomDay,m,k):
    n=len(bloomDay)
    if m*k>n:
        return -1
    
    low=min(bloomDay)
    high=max(bloomDay)
    ans=0
    while low<=high:
        mid=(low+high)//2

        if check(bloomDay,mid,k)>=m:
            ans=mid
            high=mid-1
        elif check(bloomDay,mid,k)<m:
            low=mid+1
    return ans  ## we can also return low because of the opposite polarity


bloomDay=[1,10,3,10,2]
m=3
k=1
bloomDay=[7,7,7,7,13,11,12,7]
m=2
k=3
print(minDays(bloomDay,m,k))
