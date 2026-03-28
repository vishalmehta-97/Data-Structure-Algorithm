''' Counting Frequencies of Array Elements'''

def array():
    array=[]
    n=int(input("No of Elements:"))
    for i in range(1,n+1):
        arr=int(input(f"Enter the {i} Elements:"))
        array.append(arr)
    print(array)
    return array
        
def freq(array):
    # freq=[0]*101  ## Array Mapping
    # for i in array:
    #     freq[i]+=1
    # print(freq)
    # return freq

    freq={}    ## Hash Mapping
    for i in array:
        freq[i]=freq.get(i,0)+1
    print(freq)
    return freq

def fetch(freq):
    n=int(input("Enter no of queries : "))
    for _ in range(n):
        q=int(input("Enter the No. to Fetch the Frequency : "))
        print(f"{q} no. Appeared {freq[q]} time in the Array")

# a=array()
# f=freq(a)
# fetch(f)



arrayy=[1,2,7,3,4,5,2,6,7]
n=int(input("Enter the no of querries:"))
for i in range(n):
    qu=int(input("Enter the no you want to fetch:"))
    count=0
    for _ in arrayy:
        if _ == qu :
            count+=1
    print(f"{qu} appeared {count} times")