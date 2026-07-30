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
    
    
            
    ''' Brute Force Approach '''

    def removeNthFromEnd(self, head,n):
        if head==None:
            return None
        if head.next==None and n==1:
            return None

        t1=head
        count=0
        while t1:
            count+=1
            t1=t1.next
        t2=head

        if n==count:
            head=head.next 
            return head

        while t2:
            if count==n+1:
                t2.next=t2.next.next
                break
            count-=1
            t2=t2.next
        delete_node=t1.next  ## These 2 lines are not Crucial
        t1.next=t1.next.next

        return head
    
    ''' Optimal Approach '''

    def removeNthFromEnd_(self, head,n):
        slow=head
        fast=head

        for _ in range(n):
            fast=fast.next
        
        if fast==None:
            return head.next

        while fast.next:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next

        return head



if __name__ == "__main__":
    sol = Solution()

    test_list_1 = sol.create_linked_list([1,2,3,4,5])
    ele=2
    print("Ans: ", sol.removeNthFromEnd_(test_list_1,ele))
