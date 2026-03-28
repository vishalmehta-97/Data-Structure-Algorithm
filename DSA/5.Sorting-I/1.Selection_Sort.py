def array():
    arr=[]
    n=int(input("No of elements in array :"))
    for _ in range(n):
        e=int(input(f"{_+1} element:"))
        arr.append(e)
    print(arr)
    return arr
    
def selectionS(array):
    for i in range(0,len(array)-1):
        min=i
        for j in range(i,len(array)):
            if array[j]<array[min]:
                min=j
        print(array[j],array[i])
        array[i],array[min]=array[min],array[i] 

    print(array)


a=array()
selectionS(a)