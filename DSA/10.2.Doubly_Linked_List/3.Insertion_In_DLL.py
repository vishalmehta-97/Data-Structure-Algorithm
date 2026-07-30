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

    def InsertionBeforeHead(self,node):
        temp=Node(node)
        if self.head==None:
            self.head=temp
            return "Head-->", self.head.data


        t1=self.head
        self.head=temp
        temp.next=t1
        t1.prev=temp

        return "head-->",self.head.data

    def InsertionBeforeTail(self,node):
        temp=Node(node)

        if self.head==None:
            self.head=temp
            return "Head-->" ,temp.data
        
        if self.head.next==None:
            temp.next=self.head
            self.head.prev=temp
            self.head=temp

            return "head-->",self.head.data

        t1=self.head
        while t1.next!=None:
            t1=t1.next

        temp.prev=t1.prev
        temp.next=t1
        t1.prev.next=temp
        t1.prev=temp

        return "head-->", self.head.data     
        
    def Insertion_Before_KthElement(self,node,k):
        count=1
        temp=Node(node)
        if self.head==None:
            self.head=temp

            return "Head-->",self.head.data
        
        if self.head.next==None:
            if k==1:
                return self.InsertionBeforeHead(node)
            else:
                return "Index Does not exist"
    
        t1=self.head
        while t1!=None:
            if count==k:
                break
                 
            t1=t1.next
            count+=1

        if t1==None:
            return "Index Does not exist"
        
        previous=t1.prev
        if previous==None:
            return self.InsertionBeforeHead(node)

        temp.next=t1
        temp.prev=previous
        t1.prev.next=temp
        t1.prev=temp

        return "head-->", self.head.data
    

    def InsertionBeforeNode(self,g_node,node):
        temp=Node(node)
        if self.head==None:
            return " Given node does not exist "
        
        if g_node==self.head.data:
            if self.head.next==None :
                self.head.prev=temp
                temp.next=self.head
                self.head=temp
            
                return "head-->", self.head.data
            else:
                self.head.prev=temp
                temp.next=self.head
                self.head=temp

                return "head-->", self.head.data

        
        t1=self.head
        while t1:
            if t1.data==g_node:
                break

            t1=t1.next

        if t1==None:
            return "Node Does not exist"
        

        previous=t1.prev
        temp.next=t1
        temp.prev=previous
        t1.prev.next=temp
        t1.prev=temp

        return "head-->",self.head.data    

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
array=[1,2,3,4,6]
obj.ArrayToLinkedList(array)
# print(obj.InsertionBeforeHead(1))
# print(obj.InsertionBeforeTail(6))
# print(obj.Insertion_Before_KthElement(15,5))
print(obj.InsertionBeforeNode(1,100))

obj.printLinkedL()