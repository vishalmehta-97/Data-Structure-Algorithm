''' Brute Force Approach This will give TLE '''

import math
def banana(piles,h):
    total_hrs=0
    j=1

    while True:
        total_hrs=0
        for pile in piles:
            total_hrs+=math.ceil(pile/j)
        if total_hrs<=h:
            return j 
        j+=1
        
piles=[3,6,7,11]
h=8

# print(banana(piles,h))


''' Optimal Approach '''
import math
def check(mid,piles):
    hrs=0
    for pile in piles:
        hrs+=math.ceil(pile/mid)
    print("hrs",hrs)
    return hrs

def kokoBananas(piles,h):
    low=1
    high=max(piles)
    ans=0
    while low<=high:
        mid=(low+high)//2
        print("mid",mid)
    
        if check(mid,piles)<=h:            
            ans=mid
            high=mid-1
        else:
            low=mid+1

    return ans  ## we can also return high or low that will also represent the answer

piles=[3,6,7,11]
piles=[30,11,23,4,20]
h=5 
print(kokoBananas(piles,h))
