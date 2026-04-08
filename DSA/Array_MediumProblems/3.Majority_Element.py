def majority_Element(arr):
    freq={}
    n=len(arr)

    for i in arr:
        freq[i]=freq.get(i,0)+1
    # max_key = max(freq, key=lambda x: freq[x])
    # return max_key
    for key,val in freq.items():
        if val>n//2:
            return key
    return -1

arr=[2,2,1,1,2,2]
# print(majority_Element(arr))

'''Optimal Solution using Moore's Voting Algorithm'''
def majority_element_optimal(arr):  
    n=len(arr)
    element=arr[0]
    count=0
    for i in range(n):
        if count==0:
            element=arr[i]
            if element==arr[i]:
                count+=1
            else:
                count-=1
        elif element==arr[i]:
                count+=1
        else:
            count-=1

    for j in range(n):
        if arr[j]==element:
                count+=1
    if count>(n//2):
        return element
            
    return -1

arr=[2,2,1,1,2,2]
arr=[3,2,3,2]
arr=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
print(majority_element_optimal(arr))