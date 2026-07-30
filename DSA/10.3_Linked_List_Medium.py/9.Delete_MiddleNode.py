class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''Optimal Approach'''

    def deleteMiddle(self, head):
        if head==None or head.next==None:
            return None

        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            previous=slow
            fast=fast.next.next
            slow=slow.next

        previous.next=slow.next

        return head