class Solution:
    def prefix_to_postfix(self,s):
        stack=[]
        operators=["^","*","/","+","-"]
        for i in range(len(s)-1,-1,-1):
            if s[i] not in operators:
                stack.append(s[i])
            else:
                first=stack.pop()
                second=stack.pop()
                value=first+second+str(s[i])
                stack.append(value)  

        return stack[-1]
      
ss=Solution()
s="/-ab*+def"
print(ss.prefix_to_postfix(s))

