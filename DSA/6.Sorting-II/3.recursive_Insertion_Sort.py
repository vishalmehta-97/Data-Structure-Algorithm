
def insertion_sort(array,i,n):
    if i==n:
        print(array)
        return

    key=array[i]        
    j=i-1
    while j>=0 and array[j]>key:
        array[j+1]=array[j]
        j-=1
    
    array[j+1]=key
    insertion_sort(array,i+1,n)

array = [13, 46, 24, 52, 20, 9]
insertion_sort(array, 0, len(array))
