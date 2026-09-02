class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class SinglyLinkedList:
    def __init__(self,head=None,size=0):
        self.head=head
        self.size=size

    def push(self,value):
        temp=Node(value)
        self.size+=1
        temp.next=self.head
        self.head=temp

    def pop(self):
        if self.head==None:
            print("Stack is Already Empty")
            return
        value=self.head
        self.head=self.head.next
        self.size-=1
        return value

    def topOfStack(self):
        if self.head is None:
            return None
        
        return "Top-->",self.head.data

    def isEmpty(self):
        return self.head is None

    def sizeOfStack(self):
        return "Size-->",self.size

obj=SinglyLinkedList()
print(obj.push(10))
print(obj.push(20))
print(obj.push(30))
print(obj.topOfStack())
print(obj.pop())
print(obj.topOfStack())
print(obj.sizeOfStack())

