''' Implementing Stack Using Arrays '''

class Stack:
    def __init__(self,size):
        self.size=size
        self.stack=[0]*size
        self.top=-1

    def push(self,value):
        if self.top==self.size-1:
            print("Stack Overflow")
            return
        self.top+=1
        self.stack[self.top]=value
        return self.stack

    def pop(self):
        if self.top==-1:
            print("Stack Underflow")
            return
        value=self.stack[self.top]
        self.top-=1
        return "Poped_element-->",value       

    def peek(self):  ## CHECKING THE TOP ELEMENT 
        if self.top==-1:
            print("Stack is Empty")
            return None
        return "Top-->",self.stack[self.top]

    def sizeOf(self):
        return 'Size-->', self.top+1

    def isEmpty(self):
        return self.top==-1
    
    def isFull(self):
        return self.top==self.size-1

# s=Stack(size=5)
# print(s.push(10))
# print(s.push(20))
# print(s.push(30))
# print(s.peek())
# print(s.sizeOf())
# print(s.pop())
# print(s.pop())
# print(s.peek())
# print(s.isEmpty())


''' Implementing Queue Using Arrays '''

class Queue:
    def __init__(self,size):
        self.size=size
        self.queue=[0]*size
        self.currSize=0
        self.start=-1
        self.end=-1

    def push(self,value):
        if self.currSize==self.size-1:
            print("Queue is full")
            return
        
        if self.currSize==0:
            self.start+=1
        self.end=(self.end+1)%self.size
        self.queue[self.end]=value
        self.currSize+=1

        return "After Push",self.queue

    def top(self):
        if self.start==-1:
            print("Queue is Empty")
            return
        print(self.queue)
        return "top->",self.queue[self.start]

    def pop(self):
        if self.currSize==0:
            print("Queue is Already Empty")
            return
        ele=self.queue[self.start]
        if self.currSize==1:
            self.currSize-=1
            self.start=-1
            self.end=-1
            return self.queue,"start-->",self.start,"end-->", self.end ,"pop-->",ele
        
        self.start=(self.start+1)%self.size
        self.currSize-=1
        return self.queue,"start-->",self.start,"end-->", self.end ,"pop-->",ele

    def sizeQueue(self):
        return self.currSize


q=Queue(4)
q.push(10)
q.push(20)
q.push(30)
print(q.top())
print(q.pop())
print(q.top())
q.push(40)
print(q.pop())
print(q.top())
print(q.push(50))
print(q.sizeQueue())
print(q.top())
print(q.pop())




        