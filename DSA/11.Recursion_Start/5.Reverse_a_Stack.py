class Solution:
    def interChange_Ele(self,stack,value):
        if len(stack)==0:
            stack.append(value)
            return stack
        
        old_value=stack.pop()
        self.interChange_Ele(stack,value)
        stack.append(old_value)
        return stack
    def reverseStack(self,stack):
        # if len(stack)==1 or len(stack)==0:   ## 0 will handle the base case
        if len(stack)<=1:
            return stack

        value=stack.pop()
        self.reverseStack(stack)
        return self.interChange_Ele(stack,value)



s=Solution()
stack=[]
print(s.reverseStack(stack))