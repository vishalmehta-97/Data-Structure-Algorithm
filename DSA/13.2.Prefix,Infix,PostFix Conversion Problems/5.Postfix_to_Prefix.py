class Solution:
    def postfix_to_prefix(self,s):
        stack=[]
        operators=["^","*","/","+","-"]
        for chr in s:
            if chr not in operators:
                stack.append(chr)
            else:
                second=stack.pop()
                first=stack.pop()
                value=str(chr)+first+second
                stack.append(value)  

        return stack[-1] 
      
ss=Solution()
s="ab-de+f*/"
print(ss.postfix_to_prefix(s))