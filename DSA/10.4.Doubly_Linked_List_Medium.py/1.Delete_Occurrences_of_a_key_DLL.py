class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:

    '''Code is optimal but there were some bugs in that'''

    # def deleteAllOccurrences(self, head, target):
        # t1=head
        # while t1:
        #     if t1.val==target:
        #         next_node=t1.next
        #         if t1==head:
        #             if head.next==None or head==None:
        #                 return None
        #             old_head=head
        #             head=head.next
        #             old_head.next=None
        #             t1=next_node
        #             head.prev=None

        #         elif t1.next==None:
        #             next_node=t1.next
        #             t1.prev.next=None
        #             t1.prev=None
        #             t1=next_node

        #         else:
        #             next_node=t1.next
        #             t1.prev.next=t1.next
        #             t1.next.prev=t1.prev
        #             t1.prev=None
        #             t1=next_node
                
        #     else:
        #         t1=t1.next
        # return head
    
    ''' Optimal Approach '''

    def deleteAllOccurrences_(self, head, target):
        t1=head
        while t1:
            if t1.val==target:
                if t1==head:
                    head=head.next
                    
                next_node=t1.next
                previous=t1.prev

                if next_node:
                    next_node.prev=previous

                if previous:
                    previous.next=next_node

                t1=t1.next
               
            else:
                t1=t1.next

        return head
            

        

            
