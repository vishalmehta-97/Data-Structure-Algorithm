# array=[2,3,5,6,3,2,21,97]

# freq={}

# for i in array:
#     freq[i]=freq.get(i,0)+1
# print(freq.get(7))


''' Hashing Using Key Value Pair '''

def aRray():
    array=[]
    n=int(input("total no of elements : "))
    for _ in range(n):
        elements=int(input("Enter the no:"))
        array.append(elements)
    print(array)
    return array

def Hash(array):
    freq={}
    for i in array:
        freq[i]=freq.get(i,0)+1
    for key, value in freq.items():
        print(key, "-->", value)
    return freq

def fetch(freq):
    inp=int(input("No of Queries : "))
    for _ in range(inp):
        q=int(input("No you want fetch : "))
        print(f"{q} appears {freq.get(q,0)} times")

list=aRray()
freq=Hash(list)
fetch(freq)