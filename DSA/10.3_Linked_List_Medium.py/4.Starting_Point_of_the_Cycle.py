
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    ''' Brute  Force '''
    def detectCycle(self,head):
        hash={}
        count=-1
        t1=head
        while t1:
            count+=1
            if t1 in hash:
                head=t1
                return head
            hash[t1]=count
            t1=t1.next
        return 
    
    ''' Optimal Approach '''

    def detectCycle(self,head):
        slow=head
        fast=head
        
        while fast!=None or fast.next!=None:
            slow=slow.next
            fast=fast.next.next

            if fast==slow:
                slow=head
                while fast!=slow:
                    slow=slow.next
                    fast=fast.next
                return slow

        return None
    


            