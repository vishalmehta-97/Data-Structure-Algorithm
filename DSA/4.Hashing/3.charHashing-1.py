'''CHAR HASHING'''

# Brute Force

# s="abcdabcfc"
# print(s)
# l=len(s)
# print(l)

# q=int(input("No of Queries: "))

# for _ in range(q):
#     user=input("char name for frequency:").lower()
#     count=0
#     for i in range(l):
#         if s[i]==user:
#             count+=1
#     print(count)

    # timeCOMPLEXITY = O(q x l)



''' Now the array Hashing for CHARACTERS'''

# ASCII Code of (A)-chr(65)
# ASCII Code of (Z)-chr(90)
# ASCII Code of (a)-chr(97)
# ASCII Code of (z)-chr(122)

def charHashing():
    str=input("Enter the characters(String) : ")
    array=[0]*26
    return str,array

def freq(str,array):
    for i in range(len(str)):
        array[ord(str[i])-ord('a')]+=1
    print(array)
    return array

def fetch(array):
    q=int(input("No of Queries : "))
    for _ in range(q):
        chr=input("Which Chr you want to fetch : ").lower()
        print(f"{chr} Character occured {array[ord(chr)-ord('a')]} times")

s,array=charHashing()
arr=freq(s,array)
fetch(arr)
