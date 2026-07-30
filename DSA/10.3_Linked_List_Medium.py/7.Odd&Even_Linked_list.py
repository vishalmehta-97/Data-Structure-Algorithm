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
    
    ''' Brute Force Apporach '''
    def oddEvenList(self,head):
        if head==None or head.next==None:
            return head

        array=[]
        odd=head
        while odd and odd.next!=None:
            array.append(odd.val)
            odd=odd.next.next
        if odd:
            array.append(odd.val)

        even=head.next
        while even and even.next!=None:
            array.append(even.val)
            even=even.next.next
        if even:
            array.append(even.val)

        t1=head
        count=0

        while t1:
            t1.val=array[count]
            count+=1
            t1=t1.next
            
        return head
    
    ''' Optimal Approach '''

    def oddEvenList(self,head):
        if head==None or head.next==None:
            return head
        
        odd=head
        even=head.next
        even_head=even
        while even!=None and even.next!=None:

            odd.next=odd.next.next
            even.next=even.next.next
            odd=odd.next
            even=even.next

        odd.next=even_head

        return head
            
        
if __name__ == "__main__":
    sol = Solution()

    test_list_1 = sol.create_linked_list([1,2,3,4,5,6])
    print("Method 3 (Optimal):", sol.oddEvenList(test_list_1))