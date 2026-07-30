''' This is a Normal Approach '''

def largestOddNumber(num):
    for i in range(len(num)-1,-1,-1):
        if (int(num[i]))%2!=0:
            return num[:i+1]

    return ""

num="52" 
num="4206" 
# num="35427" 
print(largestOddNumber(num))

'''This Approach is According to some TestCases (e.g-->num="004722")'''

def largestOddNumber_(num):
    ind=-1
    i=0
    for i in range(len(num)-1,-1,-1):
        if (int(num[i]))%2!=0:
            ind=i
            break
    j=0
    while j<=ind and num[i]=="0":   ## this is checking whether has zero in the start or not
        j+=1
    
    return num[j:ind+1]

num="52" 
num="4206" 
# num="35427" 
print(largestOddNumber_(num))
