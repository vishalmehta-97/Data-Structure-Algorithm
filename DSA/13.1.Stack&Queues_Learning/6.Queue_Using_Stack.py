''' Approach-I'''

class Queue:
    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]

    def push(self,x):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        self.in_stack.append(x)
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
        
    def pop(self):
        return self.in_stack.pop()

    def top(self):
        return self.in_stack[-1]

    def isEmpty(self):
        return len(self.in_stack)==0 and len(self.out_stack)==0

    
q=Queue()
print(q.isEmpty())
q.push(10)
q.push(20)
q.push(30)
print(q.top())
print(q.pop())
print(q.top())
print(q.isEmpty())

'''Approach-II'''

class Queue:
    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]

    def push(self,x):
        self.in_stack.append(x)
        
    def pop(self):
        if len(self.out_stack)!=0:
            return self.out_stack.pop()
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack.pop()

    def top(self):
        if len(self.out_stack)!=0:
            return self.out_stack[-1]
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack[-1]

    def isEmpty(self):
        return len(self.in_stack)==0 and len(self.out_stack)==0

    
q=Queue()
print(q.isEmpty())
q.push(10)
q.push(20)
q.push(30)
print(q.top())
print(q.pop())
print(q.top())
print(q.isEmpty())