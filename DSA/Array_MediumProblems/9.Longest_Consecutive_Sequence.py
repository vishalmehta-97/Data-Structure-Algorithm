'''Brute Force'''

def check_check(nums,x):
    n=len(nums)
    for j in range(n):
        if nums[j]==x+1:
            return True
    return False

def Longest_Cosecutive_Sequence(nums):
    n=len(nums)
    length=1

    for i in range(n):
        x=nums[i]
        count=1
        while check_check(nums,x)==True:
            count+=1
            x+=1
            
        if count>length:
         length=count

    return length


nums=[100,4,200,1,3,2]
# print(Longest_Cosecutive_Sequence(nums))

'''Better Aproach'''

def Longest_Consecutive_Seq_Better(nums):
    nums.sort()
    n=len(nums)
    if n==0:
        return 0

    longest=1
    # last_Smaller=min(nums)    ## intead of this we have to do this
    last_Smaller=float('-inf')  ## Negative Infinite No.
    curr_Count=0 #if we are going to use the first one we have to put 1 instead of 0 here

    for i in range(n):
        if nums[i]-1==last_Smaller:
            curr_Count+=1
            last_Smaller=nums[i]
           
        elif nums[i]!=last_Smaller:
            curr_Count=1
            last_Smaller=nums[i]

        longest=max(longest,curr_Count)

    return longest


nums=[100,102,100,101,101,4,3,2,3,2,1,1,1,2]
# nums=[100,4,200,1,3,2]
# print(Longest_Consecutive_Seq_Better(nums))



'''Optimal Solution (This Solution is Optimal Only under some constraints )'''


def longest_Consecutive_Seq_Optimal(nums):
    n=len(nums)
    if n == 0:
            return 0 

    s=set(nums)
    longest=1

    for i in s:
        if i-1 not in s:
            count=1
            first_seq=i
            while first_seq+1 in s:
                first_seq+=1
                count+=1
            longest=max(longest,count)
    return longest

nums=[102,4,100,1,101,3,2,1,1]
print(longest_Consecutive_Seq_Optimal(nums))
