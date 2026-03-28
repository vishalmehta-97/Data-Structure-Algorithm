def removeDuplicates(nums):
    n=len(nums)
    unique=set()
    for i in range(n):
        unique.add(nums[i])

    unique=list(unique)
    no=len(unique)

    for j in range(len(unique)):
        nums[j]=unique[j]

    return no, nums[:no]
          

nums=[1,1,2]
# print(removeDuplicates(nums))

def removeDuplicateOpt(nums):
    n=len(nums)
    i=1
    j=1

    for k in range(n-1):
        if nums[i]==nums[k]:
            i+=1
        else:
            nums[j]=nums[i]
            j+=1
            i+=1
    print(nums)    
    return j



nums=[1,1,1,1,2,2,3,3]
print(removeDuplicateOpt(nums))