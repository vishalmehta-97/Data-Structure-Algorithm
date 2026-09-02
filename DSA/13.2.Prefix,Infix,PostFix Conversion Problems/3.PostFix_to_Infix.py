class Solution:
    def postfix_to_infix(self,s):
        stack=[]
        operators=["^","*","/","+","-"]
        for chr in s:
            if chr not in operators:
                stack.append(chr)
            else:
                s=stack.pop()
                f=stack.pop()
                value='('+f+str(chr)+s+')'
                stack.append(value)   
        return stack[-1]     
      
ss=Solution()
s="ab-de+f*/"
print(ss.postfix_to_infix(s))

