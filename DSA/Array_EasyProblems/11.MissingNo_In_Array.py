'''This is Also optimal
Instead of this we can also do the array Mapping(HASHING)'''

def missing_element(arr):
    n=len(arr)+1
    sum_of_current_array=sum(arr)
    expSum=(n*(n+1))//2
    element =expSum - sum_of_current_array
    return element
arr=[1,2,3,5]
arr=[8,2,4,5,3,7,1]
# print(missing_element(arr))




'''This one is the most optimal which is also asked in the interview'''

''' 

This Approach is of Bitwize operator
XOR (^) Is a Bitwize Operator
where
    a^a=0
    a^0=a

    
So using this we try to solve this problem

'''

def missing_Element(arr):
    n=len(arr)+1
    xor_all=0
    xor_array=0

    for i in range(1,n+1):
        xor_all^=i

    for j in range(n-1):
        xor_array^=arr[j]

    return xor_all^xor_array


arr=[8,2,4,5,3,7,1]
arr=[5,4,2,1]
print(missing_Element(arr))