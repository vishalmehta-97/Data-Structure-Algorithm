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
array=[1,3,2,4]
obj.ArrayToLinkedList(array)
print(obj.printLinkedL())