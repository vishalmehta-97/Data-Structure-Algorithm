from collections import deque
def reverseWords(s):
    stack=deque()

    start=0
    count=0
    for i in range(len(s)):
        
        if s[i]==" ":
            stack.append(s[start:i])
            start=i
            if count==0:
                stack.append(" ") 
            count+=1
            
            
        if i==len(s)-1:
            stack.append(s[start:])
        
    ans=''    
    for _ in range(len(stack)):
        ans+=stack.pop()
    return ans

s="the sky is blue"
# print(reverseWords(s))


''' Brute Force Approach '''

def reverseWords_(s):
    words=[]
    word=""

    for chr in s:
        if chr!=" ":
            word+=chr 
        elif word:
            words.append(word)

            word=""
    if word:
        words.append(word)

    words.reverse()
    print(words)

    return " ".join(words)
    
s="the sky is blue"
print(reverseWords_(s))

''' Optimal Approach '''

def reverseWords_(s):
    s=s[::-1]
    word=""
    while 




s="the sky is blue"
# print(reverseWords_(s))