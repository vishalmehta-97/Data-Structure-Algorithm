class MinStack:
    def __init__(self):
        self.stack=[]
        
    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value,value))
        else:
            self.stack.append((value,min(value,self.stack[-1][1])))

    def pop(self) -> None:
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


s=MinStack()
 
''' Optimal Approach '''

class MinStack:
    def __init__(self,mini=float("inf")):
        self.stack=[]
        self.mini=mini
        
    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(value)
            self.mini=value
        else:
            if value<self.mini:
                self.stack.append(2*value-self.mini)
                self.mini=value
            else:
                self.stack.append(value)
                

    def pop(self) -> None:
        if not self.stack:
            return
        value=self.stack[-1]
        self.stack.pop()
        if value<self.mini:
            self.mini=(2*self.mini)-value

            

    def top(self) -> int:
        if not self.stack:
            return

        if self.stack[-1]>self.mini:
            return self.stack[-1]
        else:
            return self.mini
        
    def getMin(self) -> int:
        return self.mini


s=MinStack()
