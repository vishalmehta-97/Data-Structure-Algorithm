class Queue:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class QueueUsingLL:
    def __init__(self,start=None,end=None,size=0):
        self.start=start
        self.end=end
        self.size=size

    def push(self,value):   
        new_node=Queue(value)
        if self.start==None and self.end==None:
            self.start=new_node
            self.end=new_node
        else:
            self.end.next=new_node
            self.end=self.end.next
        self.size+=1
        return

    def pop(self):
        if self.start==None:
            print("Queue is Empty")
            return
        value=self.start.data
        if self.size==1:
            self.size-=1
            self.start=None
            self.end=None
            return value
        self.size-=1
        self.start=self.start.next
        return value

    def top(self):
        if self.size==0:
            print("Queue is Empty")
            return None
        return self.start.data

    def sizeofQueue(self):
        return self.size

q=QueueUsingLL()
q.push(10)
q.push(20)
q.push(30)
print(q.top())
print(q.pop())
print(q.pop())
print(q.top())
print(q.pop())
print(q.top())
q.push(40)
print(q.top())

