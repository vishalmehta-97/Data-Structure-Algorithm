arr=[12,-1,-7,8,-15,30,16,28]

def negativeEle(k):
    n=len(arr)
    list=[]
    right=k
    left=right-k
    
    for i in range(0,k):
        if arr[i]<0:
            list.append(arr[i])
    print(list)
    # while right<=len(arr):
    for v in range(left,right):
            if arr[v]<0:
                list.append(arr[v])
            right+=1
        
    return list

print(negativeEle(3))