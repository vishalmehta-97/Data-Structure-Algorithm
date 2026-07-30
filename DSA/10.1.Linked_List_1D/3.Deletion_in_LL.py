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
       

    def deleteNode(self,value):

        # t1=self.head
        # if self.head==None or t1.next==None:
        #     print("Null")
        #     return None
        
        # previous=t1
        # if t1.data==value:
        #     self.head=t1.next

        # while t1!=None:
        #     if t1.data==value:
        #         previous.next=t1.next
        #         break
        #     else:
        #         previous=t1
        #         t1=t1.next
            
        # t1=self.head
        # print("Head") 
        # return t1.data

        '''If we got any specific Position so we can use count in this to get the value'''

        t1=self.head
        previous=t1
        if self.head==None or t1.next==None:
            return None

        if t1.data==value:
            t1=t1.next
            return t1.data
        
        while t1!=None:
            if t1.data==value:
                previous.next=t1.next
                break
            else:
                previous=t1
                t1=t1.next

        t2=self.head
        return t2.data

    def printLinkedL(self):
        if self.head==None:
            return -1

        t1=self.head
        while (t1!=Nonace):
            print(t1.data)
            t1=t1.next
        


obj=SinglyLinkedList()
array=[13,14,44,16,18,19,5]
# array=[13]
obj.Making(array)
print(obj.deleteNode(13))
# print(obj.printLinkedL())


## Can Also use Dummy Technique for deleting the nodes in LL





