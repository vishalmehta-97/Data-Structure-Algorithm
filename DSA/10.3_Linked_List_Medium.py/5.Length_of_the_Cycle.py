class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    '''Brute Force Approach'''

    def findLengthOfLoop(self, head):
        count=-1
        hash={}

        t1=head
        while t1:
            count+=1
            if t1 in hash.keys():
            # if hash.get(t1) is not None:
                return count-hash.get(t1)
            hash[t1]=count
            t1=t1.next

        return 0

    
    ''' Optimal Approach '''
    def findLengthOfLoop(self, head):
        slow=head
        fast=head
        
        while fast and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                count=1
                fast=fast.next

                while slow!=fast:
                    fast=fast.next
                    count+=1

                return count
        return 0