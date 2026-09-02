from collections import deque

class MyStack:
    def __init__(self):
        self.stack=deque()
    
    def push(self, x: int) -> None:
        self.stack.append(x)
        s=len(self.stack)

        for _ in range(s-1):
            self.stack.append(self.stack[0])
            self.stack.popleft()

    def pop(self):
        return self.stack.popleft()

    def top(self):
        return self.stack[0]

    def isEmpty(self):
        return len(self.stack)==0

    def printStack(self):
        return self.stack

s=MyStack()
s.push(10)
print(s.printStack())
s.push(20)
print(s.printStack())
s.push(30)
print(s.printStack())
s.push(40)
print(s.printStack())
print(s.top())
s.pop()
print(s.isEmpty())
print(s.printStack())

