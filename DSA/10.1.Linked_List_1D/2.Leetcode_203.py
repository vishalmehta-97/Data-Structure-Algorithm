''' This is just the Solution Code with 2 Approaches '''

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        while head and head.val == val:
            head=head.next
        current=head
        prev=None

        while current!=None:
            if current.val==val:
                prev.next=current.next
                current=current.next
            else:
                prev=current
                current=current.next
        return head

        '''WITH DUMMY TECHNIQUE'''

        dummy=ListNode(0)
        dummy.next=head

        current=head
        prev=dummy

        while current!=None:
            if current.val==val:
                prev.next=current.next
                current=current.next
            else:
                prev=current
                current=current.next
                
        return dummy.next

