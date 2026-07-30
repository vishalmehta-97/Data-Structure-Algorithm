import heapq
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
    
    def mergeTwoSortedLL(self,head1,head2):
        t1=head1
        t2=head2

        dummy=ListNode(-1)
        temp=dummy

        while t1 and t2:
            if t1.val>=t2.val:
                temp.next=t2
                t2=t2.next
                temp=temp.next
            else:
                temp.next=t1
                t1=t1.next
                temp=temp.next
        if t1:  ## we can simply linked it to the back rather than doing manually because it is already linked
           temp.next=t1
        else:
           temp.next=t2
            
        head=dummy.next

        return head.val
                        
    
if __name__ == "__main__":
    sol = Solution()

    test_list_1 = sol.create_linked_list([2,4,8,10])
    test_list_2 = sol.create_linked_list([1,3,3,6,11,14])
    print("Method 3 (Optimal):", sol.mergeTwoSortedLL(test_list_1,test_list_2))
