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
    
    ''' Better Approach '''

    def reverse(self,head):
        if head==None and head.next==None:
            return head
        
        previous=None
        t1=head
        while t1:
            front=t1.next
            t1.next=previous
            previous=t1
            t1=front
        head=t1
        return previous
    
    def addOne(self, head):
        head=self.reverse(head)  ## Reverse the LL

        carry=1
        t1=head
        while t1 and carry!=0:
            value=t1.val
            value=value+carry
            carry=value//10
            t1.val=value%10
            t1=t1.next

        head= self.reverse(head)  ## Again Reverse the LL
        if carry!=0:
            temp=ListNode(carry)
            temp.next=head
            head=temp
            return head
        else:
            return head.val
        
    ''' Optimal Approach (Using Recursion) '''

    def helper(self,temp):
        if temp==None:
            return 1
        
        carry=self.helper(temp.next)

        temp.val=temp.val+carry

        if temp.val<10:
            return 0
    
        temp.val=0
        return 1

    def addOne(self,head):
        carry=self.helper(head)

        if carry!=0:
            newNode=ListNode(carry)
            newNode.next=head
            return newNode
        
        return head

if __name__ == "__main__":
    sol = Solution()

    test_list_1 = sol.create_linked_list([1,5,9])
    print("Method 3 (Optimal):", sol.addOne(test_list_1))




