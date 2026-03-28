def charHashing():
    str=input("Enter the characters(String) : ")
    array=[0]*256
    return str,array

def freq(str,array):
    for i in range(len(str)):
        array[ord(str[i])]+=1
    print(array)
    return array

def fetch(array):
    q=int(input("No of Queries : "))
    for _ in range(q):
        chr=input("Which Chr you want to fetch : ")
        print(f"{chr} Character occured {array[ord(chr)]} times")

s,array=charHashing()
arr=freq(s,array)
fetch(arr)
