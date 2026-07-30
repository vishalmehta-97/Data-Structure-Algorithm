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
    
    ''' Brute Force Approach '''
    def sortList(self,head):
        sort_2_array=[]

        t1=head
        while t1:
            sort_2_array.append(t1.val)
            t1=t1.next

        sort_2_array.sort()

        t1=head
        i=0
        while t1:
            t1.val=sort_2_array[i]
            i+=1
            t1=t1.next
        
        return head

    ''' Optimal Approach '''

    def mergeNodes(self,head1,head2):  ## To merge the sorted list(LL)
        # t1=head1
        # t2=head2
        dummy=ListNode(-1)
        temp=dummy

        while head1 and head2:
            if head1.val>=head2.val:
                temp.next=head2
                head2=head2.next
            else:
                temp.next=head1
                head1=head1.next

            temp=temp.next

        if head1:  
           temp.next=head1
        else:
           temp.next=head2
            
        head=dummy.next

        return head
        
    def find_middle(self,head):   ## To Find Middle
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow
    

    def sortList_(self,head):  ## Main Function (all calls are done here)
        if head==None or head.next==None:
            return head
        
        mid=self.find_middle(head)
        
        new_head=mid.next
        mid.next=None
        left_head=self.sortList_(head)
        right_head=self.sortList_(new_head)

        return self.mergeNodes(left_head,right_head)
   


if __name__ == "__main__":
    sol = Solution()

    test_list_1 = sol.create_linked_list([-1,5,3,4,0])
    print("Method 3 (Optimal):", sol.sortList_(test_list_1))
