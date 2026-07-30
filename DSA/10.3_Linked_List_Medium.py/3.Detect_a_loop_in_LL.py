
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    '''Brute Force Approach'''
    ## But this is not a Good Approach to use anywhere
    def hasCycle(self, head):
        if head==None or head.next==None:
            return False
        t1=head
        while t1:
            if t1.val==float('inf'):
                return True
            t1.val=float('inf')
            t1=t1.next
        return False
    

    '''Brute Force Approach'''

    def hasCycle(self, head):
        if head==None or head.next==None:
            return False
        visited=set()
        t1=head
        while t1:
            if t1 in visited:
                return True
            visited.add(t1)
            t1=t1.next
        return False
    
    ''' Optimal Approach '''
    
    def hasCycle(self, head):

        fast=head
        slow=head
        while fast!=None and fast.next!=None:
            if slow==fast:
                return True
            slow=slow.next
            fast=fast.next.next
        
        return False
 