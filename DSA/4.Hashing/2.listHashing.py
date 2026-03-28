# # input array
# arr = [1, 3, 2, 1, 3, 2, 1]

# # step 1: create hash list
# freq = [0] * 11   # index 0 to 10
# print(freq)

# # step 2: store frequencies
# for num in arr:
#     freq[num] += 1
# print(freq)
# # step 3: queries
# q = int(input("How many queries: "))

# for _ in range(q):
#     x = int(input("Find frequency of: "))
#     print(f"{x} occurs {freq[x]} times")




''' My Own ArrayHashing '''
def aRray():
    array=[]
    n=int(input("total no of elements : "))
    for _ in range(n):
        elements=int(input("Enter the no:"))
        array.append(elements)
    print(array)
    return array

def arrayHash(array):
    mapArray=[0]*100
    for num in array:
        mapArray[num]+=1
    return mapArray
        
def fetch(mapArray):
    inp=int(input("No of Queries : "))
    for _ in range(inp):
        q=int(input("No you want fetch : "))
        print(f"{q} appears {mapArray[q]} times")

list=aRray()
freq=arrayHash(list)
fetch(freq)