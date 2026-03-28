'''Brute Force'''
def union(arr1,arr2):
    unique_Set=set()
    
    for i in range(len(arr1)):
        unique_Set.add(arr1[i])
    for j in range(len(arr2)):
        unique_Set.add(arr2[j])

    union_list=list(unique_Set)
    return union_list

arr1=[1,1,2,3,3,4,5]
arr2=[1,2,2,3,3,5,6]

# print(union(arr1,arr2))

'''Optimal Approach'''

def union(a,ar):
    i=j=0
    union_arr=[]
    while i<len(a) and j<len(ar):
        if a[i]<=ar[j]:
            if len(union_arr)==0 or a[i] not in union_arr:
                union_arr.append(a[i])
            i+=1

        else:
            if len(union_arr)==0 or ar[j] not in union_arr:
                union_arr.append(ar[j])
            j+=1

    while j<len(a):
        if len(union_arr)==0 or ar[j] not in union_arr:
                union_arr.append(ar[j])
        j+=1

    while i<len(a):
        if len(union_arr)==0 or a[i] not in union_arr:
                union_arr.append(a[i])
        i+=1

        

    return union_arr

            


arr1=[1,1,2,3,3,4,5]
arr2=[1,2,2,3,3,5,6]

print(union(arr1,arr2))