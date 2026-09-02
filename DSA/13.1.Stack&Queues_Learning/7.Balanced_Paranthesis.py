class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
    
        for i in s:
            if i==')' and len(stack)!=0:
                
                if stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif i==']' and len(stack)!=0:
                if stack[-1]=='[':
                    stack.pop()
                else:
                    return False
            elif i=='}' and len(stack)!=0:
                if stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if len(stack)==0:
            return True
        return False

s=Solution()
ss='()[{}()]'
# ss='()[{}(])'
ss=']'
print(s.isValid(ss))

''' More Clean Code '''
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack.pop()


                if i==')' and top=='(' or i==']' and top=='[' or i=='}' and top=='{':
                    continue
                else:
                    return False
                
        return not stack
                
           
s=Solution()
ss='()[{}()]'
ss='()[{}(])'
ss=']'
print(s.isValid(ss))