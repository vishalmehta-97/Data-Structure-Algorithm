from collections import deque

class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

class DoublyLinkedList:
    def __init__(self,head=None):
        self.head=head

    def ArrayToLinkedList(self,array):
        if not array:
            print("Empty Array")
            return -1
        
        self.head=Node(array[0])
        t1=self.head

        for i in range(1,len(array)):
            t1.next=Node(array[i],t1,None)
            t1=t1.next

    def reverse_DLL(self):   ## Reversed Only in Terms of Data
        if self.head==None:
            return None

        stack=deque()

        t1=self.head
        while t1:
            stack.append(t1.data)
            t1=t1.next

        t2=self.head
        while t2:
            t2.data=stack.pop()
            t2=t2.next
        return "Head of the reversed Doubly Linked List",self.head.data
    
    def reverse_DLL_better(self):
        if self.head==None and self.head.next==None:
            return self.head


        current=self.head
        while current:
            last=current.prev
            current.prev=current.next
            current.next=last

            current=current.prev
        self.head=last.prev

    def printLinkedL(self):
            if self.head==None:
                print("Empty Linked List")
                return

            t1=self.head
            while (t1!=None):
                print(t1.data)
                t1=t1.next
            t2=self.head
            return "head-->",t2.data

obj=DoublyLinkedList()
array=[5,4,3,2,1]
obj.ArrayToLinkedList(array)
print(obj.reverse_DLL_better())
obj.printLinkedL()