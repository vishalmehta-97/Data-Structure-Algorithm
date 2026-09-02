class Solution:
    def prefix_to_infix(self,s):
        stack=[]
        operators=["^","*","/","+","-"]
        for i in range(len(s)-1,-1,-1):
            if s[i] not in operators:
                stack.append(s[i])
            else:
                sec=stack.pop()
                firs=stack.pop()
                value='('+sec+str(s[i])+firs+')'   ## This is the only change from the postfix to infix
                stack.append(value)  

        return stack[-1]     
      
ss=Solution()
s="*+pq-mn"
print(ss.prefix_to_infix(s))

