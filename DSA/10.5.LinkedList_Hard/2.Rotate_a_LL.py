class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def create_linked_list(self,elements):
        if not elements:
            return None
        head = ListNode(elements[0])
        current = head

        for val in elements[1:]:
            current.next = ListNode(val)
            current = current.next
        return head
    
    def check_length(self,head):
        count=0
        t1=head
        while t1:
            t1=t1.next
            count+=1
        return count
    
    ''' Better Approach '''

    def rotateRight(self,head,k):
        if head==None or head.next==None:
            return head
        length=self.check_length(head)
        k=k%length

        while k!=0:
            previous=None
            temp=head
            count=1
            while temp.next:
                count+=1
                previous=temp
                temp=temp.next
            previous.next=None
            temp.next=head
            head=temp
            k-=1
        return head.next.next.val
    
    ''' Optimal Approach '''

    def rotateRight_(self,head,k):
        if head==None or head.next==None:
            return head
        length=self.check_length(head)
        k=k%length
        rotation=(length-k)
        if rotation<0:
            rotation=-(rotation)

        if rotation==length:
            return head
        
        temp=head
        while rotation!=1:
            temp=temp.next
            rotation-=1
        next_node=temp.next
        temp.next=None
        new_head=next_node
        
        previous=None
        while next_node:
            previous=next_node
            next_node=next_node.next
        previous.next=head
        head=new_head
        return head

    ''' Optimal Approach '''

    def check_length(self,head):
            count=0
            t1=head
            previous=None
            while t1:
                previous=t1
                t1=t1.next
                count+=1
            return count,previous

    def rotateRight_opt(self,head,k):
        if head==None or head.next==None:
            return head
        
        length,tail_node=self.check_length(head)
        
        k=k%length
        if k%length==0:
            return head
        else:
            rotation=length-k
        
        tail_node.next=head
        temp=head
        while rotation!=1:
            rotation-=1
            temp=temp.next
        head=temp.next
        temp.next=None

        return head

        

if __name__=="__main__":
    sol = Solution()
    test_list_1 = sol.create_linked_list([10,20,30,40,50])
    k=4
    print("Ans: ",sol.rotateRight_opt(test_list_1,k))
