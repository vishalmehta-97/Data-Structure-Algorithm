from collections import deque
def removeOuterParentheses(s):
    stack=deque()
    ans=''
    for char in s:
        if char=='(':
            if stack:
                ans+=char
            stack.append(char)

        elif char==')':
            stack.pop()
            if stack:
                ans+=char
    return ans

''' Optimal Approach '''
    
    

s="(()())(())"
s="(()())(())(()(()))"
print(removeOuterParentheses(s))

def removeOuterParentheses(s):
    ans=''
    count=0
    for char in s:
        if char=='(':
            if count>0:
                ans+='('
            count+=1
            
        elif char==')':
            count-=1
            if count>0:
                ans+=')'
    return ans
    

s="(()())(())"
s="(()())(())(()(()))"
print(removeOuterParentheses(s))
            



