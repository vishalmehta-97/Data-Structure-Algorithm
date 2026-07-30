class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def segregate(self, head):
        if head==None and head.next==None:
            return head

        temp=head

        zeroHead=Node(-1)
        t0=zeroHead
        oneHead=Node(-1)
        t1=oneHead
        twoHead=Node(-1)
        t2=twoHead

        while temp:
            if temp.data==0:
                t0.next=temp
                t0=temp
            elif temp.data==1:
                t1.next=temp
                t1=temp
            else:
                t2.next=temp
                t2=temp

            temp=temp.next
        
        if oneHead.next != None:
            t0.next = oneHead.next
        else:
            t0.next = twoHead.next
        t1.next = twoHead.next
        t2.next = None
        
    
        return zeroHead

        
            


        