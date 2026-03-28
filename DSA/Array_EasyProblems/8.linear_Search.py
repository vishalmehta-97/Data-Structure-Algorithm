def linearSearch(array,num):
    n=len(array)
    for i in range(n):
        if array[i]==num:
            return i      
    return -1
array=[6,7,4,8,1,4]      
print(linearSearch(array,4))
