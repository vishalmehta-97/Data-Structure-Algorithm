from collections import deque
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
    
    '''Brute Force Approach'''

    def checkPalindrome(self,array):
        n=len(array)
        i=0
        j=n-1

        while i<j:
            if array[i]!=array[j]:
                return False
            i+=1
            j-=1
        
        return True

    def palindromeLL(self,head):
        array=[]

        t1=head
        while t1:
            array.append(t1.val)
            t1=t1.next
        return self.checkPalindrome(array)
    

    ''' Brute Force Approach '''
    
    def isPalindrome(self,head):
        stack=deque()
        t1=head
        while t1:
            stack.append(t1.val)
            t1=t1.next
        
        t2=head
        while t2:
            if t2.val!=stack.pop():
                return False
            t2=t2.next

        return True

    ''' Optimal Approach '''

    def reverse(self,head):
        previous=None
        t1=head

        while t1:
            front=t1.next
            t1.next=previous
            previous=t1
            t1=front
        head=previous
        return head

    def isPalindrome_(self,head):
        slow=head
        fast=head

        while fast.next!=None and fast.next.next!=None:
            slow=slow.next
            fast=fast.next.next

        mid=slow.next
        first=head
        
        ## reverse Call
        new_head=self.reverse(mid)
        last=new_head

        while last:
            if first.val!=last.val:
                self.reverse(new_head)
                return False
            first=first.next 
            last=last.next 

        self.reverse(new_head)
        return True
        


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: A valid palindrome [1, 2, 2, 1]
    # FIXED: Added 'sol.' prefix to create_linked_list
    # test_list_1 = sol.create_linked_list([1, 2, 2, 1])
    # print("Test Case 1 (Expected: True)")
    # print("Method 1 (Array):", sol.palindromeLL(test_list_1))
    
    # test_list_1 = sol.create_linked_list([1, 2, 2, 1]) 
    # print("Method 2 (Stack):", sol.isPalindrome(test_list_1))

    test_list_1 = sol.create_linked_list([1,2,3,2,1])
    print("Method 3 (Optimal):", sol.isPalindrome_(test_list_1))
    print("-" * 30)

    # Test Case 2: An invalid palindrome [1, 2, 3]
    # FIXED: Added 'sol.' prefix to create_linked_list
    # test_list_2 = sol.create_linked_list([1, 2, 3])
    # print("Test Case 2 (Expected: False)")
    # print("Method 1 (Array):", sol.palindromeLL(test_list_2))
    
    # test_list_2 = sol.create_linked_list([1, 2, 3])
    # print("Method 2 (Stack):", sol.isPalindrome(test_list_2))

    # test_list_2 = sol.create_linked_list([1, 2, 3])
    # print("Method 3 (Optimal):", sol.isPalindrome_(test_list_2))

       