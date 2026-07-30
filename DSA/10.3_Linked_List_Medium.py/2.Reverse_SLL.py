from collections import deque
class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head

    
    def Making(self,array):
        if not array:
            return "No elements"
        
        self.head=Node(array[0])   ## Initializing the head 
        t1=self.head

        for i in range(1,len(array)):
            t1.next=Node(array[i])
            t1=t1.next

    '''Brute Force Approach'''
    def reverse_SLL(self):   ## Using Stack
        stack=deque()
        t1=self.head
        while t1:
            stack.append(t1.data)
            t1=t1.next
        t1=self.head
        while t1:
           t1.data=stack.pop()
           t1=t1.next
        t1=self.head
        
    
    ''' Optimal Approach'''
    def reverse_SLL_opt(self):
        t1=self.head
        previous=None
        while t1:
            front=t1.next
            t1.next=previous
            previous=t1
            t1=front
        self.head=previous

        return "head-->",self.head.data
        
    ''' Recursive Optimal Approach'''
    def recursive_reverse_SLL_opt(self):   ## Here we have used the extra function because of the parameter issue which i was facing while implementing this
        self.head=self._reverse(self.head)

    def _reverse(self,head):
        if head==None or head.next==None:
            return head
        
        new_head=self._reverse(head.next)
        front=head.next
        front.next=head
        head.next=None

        return new_head

    
    def printLinkedL(self):
        if self.head==None:
            return -1

        t1=self.head
        while (t1!=None):
            print(t1.data)
            t1=t1.next


        

obj=SinglyLinkedList()
array=[5,4,3,2,1]
obj.Making(array)
print(obj.recursive_reverse_SLL_opt())
print(obj.printLinkedL())








