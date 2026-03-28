'''Brute Force (not optimal for worst case)'''

def intersection_brute(arr1,arr2):
    track=[0]*len(arr2)
    intersection_arr=[]
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i]==arr2[j] and track[j]==0:
                print(arr1[i])
                intersection_arr.append(arr1[i])
                track[j]=1
                break
            if arr1[i]<arr2[j]:
                break
    return intersection_arr

arr1=[1,2,2,3,3,4,5,6]
arr2=[2,3,3,5,6,6,7]

# print(intersection_brute(arr1,arr2))


def intersection_optimal(a,b):
    i=j=0
    intersection_array=[]
    while i < len(a) and j < len(b):
        if a[i]!=b[j]:
            if a[i]<b[j]:
                i+=1
            else:
                j+=1
        else:
            intersection_array.append(a[i])
            i+=1
            j+=1
    return intersection_array

a=[1,2,2,3,3,4,5,6]
b=[2,3,3,5,6,6,7]

print(intersection_optimal(a,b))


