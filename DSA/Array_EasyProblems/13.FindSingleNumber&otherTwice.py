'''Brute Force (This Solution will not pass all the test cases in leetcode)'''

# def singleNo(arr):
#     n=len(arr)
#     for i in range(n):
#         count=0
#         num=arr[i]
#         for j in range(n):
#             if arr[j]==num:
#                 count+=1
#         if count==1:
#             return num


arr=[1,1,2,3,3,4,4]
# arr=[2,2,1]
# arr=[4,1,2,1,2]
# arr=[-1]
# print(singleNo(arr))


'''This One is also not optimal because this doesn't work for negative elements '''
def singleNo(arr):
    n=len(arr)
    a=[0]*(max(arr)+1)

    for i in range(n):
        a[arr[i]]+=1

    for j in range(len(a)):
        if a[j]==1:
            return j
        
arr=[1,1,2,3,3,4,4]
arr=[-1]
# print(singleNo(arr))  

''' So we'll be going with the HashMaps(Dict) '''
 
def single_Element(arr):
    freq={}
    for x in arr:
        freq[x]=freq.get(x,0)+1
    for key, value in freq.items():
        if value == 1:
            return key  
     

arr=[1,1,2,3,3,4,4]
arr=[-1]
# print(single_Element(arr))



def single(arr):
    xor=0
    for i in range(len(arr)):
        xor^=arr[i]
    return xor

arr=[1,1,2,3,3,4,4]
# arr=[-1]
print(single_Element(arr))