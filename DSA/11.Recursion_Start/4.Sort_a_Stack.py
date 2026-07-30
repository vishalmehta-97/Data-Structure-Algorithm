class Solution:
    def insert(self,stack,value):
        if len(stack)==0 or value<=stack[-1]:
            stack.append(value)
            return stack

        big_value=stack.pop()
        self.insert(stack,value)
        stack.append(big_value)
        return stack
        

    def sortStack(self, stack):
        if len(stack)==1:
            return stack
        value=stack.pop() 
        self.sortStack(stack)
        return self.insert(stack,value)
    
            
s=Solution()
stack=[4,1,3,2]
print(s.sortStack(stack))