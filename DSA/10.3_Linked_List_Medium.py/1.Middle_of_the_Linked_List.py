class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    
class SinglyLinkedList:
    def __init__(self,head=None):
        self.head=head

    
    def Array2LinkedList(self,array):
        if not array:
            return "No elements"
        
        self.head=Node(array[0])   ## Initializing the head 
        t1=self.head

        for i in range(1,len(array)):
            t1.next=Node(array[i])
            t1=t1.next

    def middleOfLinkedList(self):
        t1=self.head
        count=0
        
        while t1:
            count+=1
            t1=t1.next

        middle_index=(count//2)+1

        t1=self.head
        counter=0
        while t1:   
            counter+=1
            if counter==middle_index:
                break
            t1=t1.next

        return t1 # ans
    
    def middleOfLL_optimal(self):   ## Optimal Approach (my own)
        if self.head.next==None:
            return self.head
        elif self.head.next.next==None:
            return self.head.next
        
        t1=self.head.next.next
        mid=self.head.next
        count=3
        while t1:
            if count%2==0:
                mid=mid.next

            t1=t1.next
            count+=1

        return mid
    
    '''More Optimal Approach (n/2)'''

    def middleOfLL_optimal_slow_fast(self):
        if self.head==None or self.head.next==None:
            return self.head
        
        slow=self.head
        fast=self.head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        return slow.data


        
    def printLinkedL(self):
        if self.head==None:
            return -1

        t1=self.head
        while (t1!=None):
            print(t1.data)
            t1=t1.next
        


obj=SinglyLinkedList()
array=[1,2,3,4,5]
array=[1,2,3,4,5,6]
obj.Array2LinkedList(array)
print(obj.middleOfLL_optimal_slow_fast())
# print(obj.printLinkedL())