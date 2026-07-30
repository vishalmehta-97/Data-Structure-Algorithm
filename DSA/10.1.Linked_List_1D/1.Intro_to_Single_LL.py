class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head

    ## Insertion in the end
    def insertAtEnd(self,value):
        temp=Node(value)
        if self.head!=None:
            t1=self.head
        
            while (t1.next!=None):
                t1=t1.next
            t1.next=temp
        else:
            self.head=temp
            self.next=None
    
    ## Insertion in the Start

    def insertatBeginning(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp

    ## Insertion in Middle

    def insertInMiddle(self,value,x):   ## Here X is the value after which we want to add the new node
        temp=Node(value)
        t1=self.head
    
        while (t1!=None):   ## this will help us to insert in the last also if the given x is already the last value
            if (t1.data==x):
                temp.next=t1.next
                t1.next=temp
                break
            else:
                t1=t1.next

    def InsertionAtKPosition(self,value,k):
        count=1

        if self.head==None:
            if k==1:
                temp=Node(value)
                self.head=temp
                return
            else:
                return None
            
        if k==1:
            temp=Node(value)
            temp.next=self.head
            self.head=temp
            return temp.data
        
        t1=self.head
        while t1!=None:
            if count+1==k:
                temp=Node(value)
                temp.next=t1.next
                t1.next=temp
                break
            
            else:
                t1=t1.next
                count+=1
        return self.head.data
    
    def deleteNode(self,value):
        t1=self.head
        previous=t1
        if t1.data==value:
            self.head=t1.next

        while t1!=None:
            if t1.data==value:
                previous.next=t1.next
                break
            else:
                previous=t1
                t1=t1.next

    def length0fLl(self):
        t1=self.head

        count=0
        while t1!=None:
            count+=1
            t1=t1.next
        return count
        
            
    def printLinkedL(self):
        t1=self.head
        len=0
        while (t1!=None):
            print(t1.data,end="--> ")
            len+=1
            t1=t1.next
        print()
        print("length of the LinkedList-->",len)
        return len

            
obj=SinglyLinkedList()

obj.insertatBeginning(5)
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertInMiddle(25,20)
obj.insertInMiddle(40,30)
obj.insertatBeginning(3)
# obj.InsertionAtKPosition(1,1)
# obj.InsertionAtKPosition(500,6)
# obj.InsertionAtKPosition(5000,9)
obj.InsertionAtKPosition(11,8)
# obj.deleteNode(3)
# obj.deleteNode(25)
obj.printLinkedL()





