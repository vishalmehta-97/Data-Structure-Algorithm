'''To do Brute Force i have do the permutation first from recursion (Brute Force approach is not good here)'''


'''Optimal
1. Longer Prefix Match
        a[i]<a[i+1]  (Break Point)
2. Find Someone greater than 1 but the smallest one so that we stay close
3. Now we hypothetuaclly say that the value going to be bigger than the old one so remaining placess will be filled with the pending elements in ascending order.

'''
def nextPermutation_optimal(nums):
    n=len(nums)
    ind=-1
    for i in range(n-1,0,-1):
        if nums[i]>nums[i-1]:
            ind=i-1 
            break
    if ind==-1:
        v=0
        l=n-1
        while v<l:
            nums[v],nums[l]=nums[l],nums[v]
            v+=1
            l-=1
            return nums
    else:
        for i in range(n-1,ind,-1):
            print(ind)
            if nums[i]>nums[ind]:
                nums[ind],nums[i]=nums[i],nums[ind]
                break
    add_ind=ind+1
    lenn=n-1
    while add_ind<lenn:
        nums[add_ind], nums[lenn] = nums[lenn], nums[add_ind]
        add_ind+= 1
        lenn-= 1
        
    # nums[ind + 1:] = reversed(nums[ind + 1:])
    return nums

# nums=[2,1,5,4,3,0,0]
nums=[3,2,1]
# nums=[1,2,3]
# nums=[1,5,1]
print(nextPermutation_optimal(nums))