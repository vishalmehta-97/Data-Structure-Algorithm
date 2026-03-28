# def array():
#     arr=[]
#     n=int(input("No of elements in array :"))
#     for _ in range(n):
#         e=int(input(f"{_+1} element:"))
#         arr.append(e)
#     print(arr)
#     return arr
array=[19,14,15,12,6,8,13]
# def insertionSort(array):
#     for i in range(len(array)):
#         j=i
#         while j>0 and array[j-1]>array[j]:
#             array[j-1],array[j]=array[j],array[j-1]
#             j-=1
#     print(array)

# def insertionSort( array):
#     n = len(array)
    
#     for i in range(1, n):
#         key = array[i] # Current element as key 
#         j = i - 1
        
#         # Shift elements that are greater than key by one position
#         while j >= 0 and array[j] > key:
#             array[j + 1] = array[j]
#             j -= 1
        
#         array[j + 1] = key # Insert key at correct position
    
#     print(array)


# # a=array()
# insertionSort(array)


def InsertionSort(array):
    for i in range(1,len(array)):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j-=1

        array[j+1]=key

    print(array)

InsertionSort(array)