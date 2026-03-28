def array():
    arr=[]
    n=int(input("No of elements in array :"))
    for _ in range(n):
        e=int(input(f"{_+1} element:"))
        arr.append(e)
    print(arr)
    return arr

def bubbleSort(array):
    for i in range(1,len(array)+1):
        l=0
        r=1
        didswap=0
        for _ in range(len(array)-i):
            if array[l]>array[r]:
                array[l],array[r]=array[r],array[l]
                didswap=1
            l+=1
            r+=1

        if didswap==0:
            break
        print("runs")
    print(array)



a=array()
bubbleSort(a)