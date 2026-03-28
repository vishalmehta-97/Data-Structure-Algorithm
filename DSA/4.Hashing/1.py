''' Freq of no's in arrray'''
## DECLARING HASHING

def inputArray():
    array=[]
    n=int(input("Enter the total length of array: "))
    for _ in range(n):
        element=int(input(f"Enter {_+1} Element: "))
        array.append(element)
    return array

def freqNumber(array):
    freq={}
    for i in array:
        freq[i]=freq.get(i,0)+1
    return freq

def fetch(freq):
    n=int(input("No of Queries: "))
    for _ in range(n):
        x=int(input("Freq of which no (elements of array):"))
        print(f"{x} --> {freq.get(x)}")

array=inputArray()
freqency=freqNumber(array)
fetch(freqency)