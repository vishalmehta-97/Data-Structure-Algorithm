''' Hashing Using Key Value Pair for String '''

def sTring():
    strr=input("Enter the String : ")
    return strr

def Hash(strr):
    freq={}
    for i in strr:
        freq[i]=freq.get(i,0)+1
    for key, value in freq.items():
        print(key, "-->", value)
    return freq

def fetch(freq):
    inp=int(input("No of Queries : "))
    for _ in range(inp):
        q=input("Word you want fetch : ")
        print(f"{q} appears {freq.get(q,0)} times")

list=sTring()
freq=Hash(list)
fetch(freq)