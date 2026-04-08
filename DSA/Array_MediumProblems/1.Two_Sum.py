'''Brute Force'''

def twoSum(array,target):

    n=len(array)
    for i in range(n):
        for j in range(i+1,n):   
            if array[i]+array[j]==target:
                return i,j

array=[2,7,11,15]
target=9
# print(twoSum(array,target))


'''Better/Optimal Approach'''

def twoSum_Hash (array,target):
    elements={}
    for i,arr in enumerate(array):
        print(i,arr)
        elem=target-arr
        if elem in elements:
            return [elements[elem],i]
        elements[elem]=i
    return [-1,-1]


array=[2,7,11,15]
target=9
# print(twoSum_Hash(array,target))


'''This is Also one optimal approach for Yes/No Question'''

def twoSum_Hash_optimal(array,target):
    i=0
    j=len(array)-1
    array.sort()

    while i<j:
        if array[i]+array[j]==target:
            return "Yes"
        elif array[i]+array[j]<target:
            i+=1
        else:
            j-=1
    return "No"

array=[3,2,4]
target=6
print(twoSum_Hash_optimal(array,target))

