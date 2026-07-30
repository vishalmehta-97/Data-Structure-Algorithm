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

    def deleteHead(self,head):

        if self.head==None:
            return head
        
        t1=self.head
        if t1.next==None:
            self.head=None
            return "Now the Linked List is empty"

        ''' Main Logic 1'''
        # t1=self.head
        # self.head=t1.next
        
        # self.head.prev=None
        # t1.next = None

        ''' Main Logic 2'''
        # t1=self.head
        # self.head=self.head.next
        # self.head.prev=None
        # t1.next=None

        # t2=self.head
        # return "head-->",t2.data
    
    def deleteTail(self,head):
        if self.head==None:
            return None

        if self.head.next==None:
            self.head=None
            return self.head
        
        t1=self.head
        while t1.next!=None:
            t1=t1.next
        previous=t1.prev
        t1.prev=None
        previous.next=None
        
        return previous.data
    
    def deletionKthElement(self,k):
        count=0
        if self.head==None:
            return "List is Empty"

        if self.head.next==None and k==1:
            self.head=None
            return None

        if count==k-1:
            t1=self.head
            self.head=self.head.next
            self.head.prev=None
            t1.next=None
            return " Head--> ",self.head.data
    
        t1=self.head
        while t1!=None:
            if count==k-1:
                if t1.next==None:
                    t1.prev.next=None
                    t1.prev=None
                    return  "head-->",self.head.data

                else:
                    previous=t1.prev
                    previous.next=t1.next
                    t1.next.prev=previous
                    t1.prev=None
                    t1.next=None
                    return self.head.data
                
        
            t1=t1.next
            count+=1

   
        return "index doesnt exist"

    ''' This Block of Code is from Striver Logic which is clean and resusable '''
    def deletionKthElement(self, k):

        if self.head is None:
            return None

        count = 1
        t1 = self.head

        # Find the kth node
        while t1 is not None:
            if count == k:
                break
            t1 = t1.next
            count += 1

        # k is greater than length
        if t1 is None:
            return "Index doesn't exist"

        previous = t1.prev
        front = t1.next

        # Only one node in the list
        if previous is None and front is None:
            self.head = None
            return None

        # Delete Head
        elif previous is None:
            return self.deleteHead(self.head)

        # Delete Tail
        elif front is None:
            return self.deleteTail(self.head)

        # Delete Middle
        previous.next = front
        front.prev = previous
        t1.prev = None
        t1.next = None

        return self.head
    
    def deleteGivenNode(self,value):

        if self.head==None:
            return None

        if self.head.next==None and value==self.head.data :
            self.head=None
            return None
        
        t1=self.head

        if t1.data==value:
            self.head=t1.next
            t1.next=None
            self.head.prev=None
            return 'head-->',self.head.data

        while t1:
            if t1.data==value:
                if t1.next==None:
                    previous=t1.prev
                    t1.prev=None
                    previous.next=None
                    return "head-->",self.head.data
                previous=t1.prev
                front=t1.next
                previous.next=front
                front.prev=previous
                t1.prev=None
                t1.next=None

                return "head-->",self.head.data
            
            else:
                t1=t1.next
        return "Value does not exist"
    
    def deleteNode(self, temp):    ## Striver's Version

        if temp is None:
            return

        previous = temp.prev
        front = temp.next

        # If temp is the last node (tail)
        if front is None:
            previous.next = None
            temp.prev = None
            return

        # Delete middle node
        previous.next = front
        front.prev = previous

        temp.prev = None
        temp.next = None



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
array=[1,2,3,4]
obj.ArrayToLinkedList(array)
# print(obj.deleteHead(1))
# print(obj.deleteTail(4))
# print(obj.deletionKthElement(4))
print(obj.deleteGivenNode(5))
print(obj.printLinkedL())

