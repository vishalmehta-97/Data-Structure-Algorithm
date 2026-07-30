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
    
    '''Better Approach'''
    def addTwoNumbers(self,l1,l2):
        t1=l1
        t2=l2
        carry=0
        array=[]

        while t1 and t2:    

            value=t1.val+t2.val+carry
            carry=value//10
            value=value%10
            # t1.val=value
            array.append(value)
            t1=t1.next
            t2=t2.next

        while t1:
            value=t1.val+carry
            carry=value//10
            value=value%10
            array.append(value)
            # t1.val=value

            t1=t1.next

        while t2:
            value=t2.val+carry
            carry=value//10
            value=value%10
            array.append(value)
            # t1.val=value

            t2=t2.next

        if carry!=0:
            array.append(carry)

        return self.create_linked_list(array).next.val

    '''Better Approach (Same like the previous one just slight changes)'''

    def addTwoNumbers_(self,l1,l2):
        t1=l1
        t2=l2
        carry=0
        array=[]
        
        while t1 and t2:    

            value=t1.val+t2.val+carry
            carry=value//10
            value=value%10
            # t1.val=value
            array.append(value)
            t1=t1.next
            t2=t2.next
        which_ll=0
        while t1:
            which_ll=1
            value=t1.val+carry
            carry=value//10
            value=value%10
            array.append(value)
            # t1.val=value

            t1=t1.next

        while t2:
            which_ll=-1
            value=t2.val+carry
            carry=value//10
            value=value%10
            array.append(value)
            # t1.val=value
            t2=t2.next
        if carry!=0:
            array.append(carry)
            carry_node=ListNode(carry)

        if which_ll==1:
            t1=l1
            i=0
            while t1:
                t1.val=array[i]
                i+=1
                if t1.next==None:
                    prev=t1
                t1=t1.next
            if carry!=0:
                prev.next=carry_node
                return l1
            return l1

        else:
            t2=l2
            i=0
            while t2:
                t2.val=array[i]
                i+=1
                if t2.next==None:
                    prev=t2
                t2=t2.next

            if carry!=0:
                prev.next=carry_node
                return l2
            return l2


    '''Optimal Approach'''

    def addTwoNumbers_opt(self,l1,l2):
        t1=l1
        t2=l2
        carry=0
        dummy=ListNode(-1)
        temp=dummy
        while t1 and t2:    

            value=t1.val+t2.val+carry
            carry=value//10
            value=value%10
            new_node=ListNode(value)
            temp.next=new_node
            temp=temp.next
            t1=t1.next
            t2=t2.next

        while t1:
            value=t1.val+carry
            carry=value//10
            value=value%10
            new_node=ListNode(value)
            temp.next=new_node
            temp=temp.next

            t1=t1.next

        while t2:
            value=t2.val+carry
            carry=value//10
            value=value%10
            new_node=ListNode(value)
            temp.next=new_node
            temp=temp.next

            t2=t2.next

        if carry!=0:
            new_node=ListNode(carry)
            temp.next=new_node

        return dummy.next
    
    def addTwoNumbers_optimal(self,l1,l2):

        dummy=ListNode(-1)
        temp=dummy
        carry=0
        while l1 or l2 or carry!=0:
            sum=0
            if l1 is not None:
                sum+=l1.val
                l1=l1.next

            if l2 is not None:
                sum+=l2.val
                l2=l2.next

            sum=sum+carry
            carry=sum//10
            new_Node=ListNode(sum%10)
            temp.next=new_Node
            temp=temp.next

        return dummy.next

    
if __name__ == "__main__":
    sol = Solution()

    test_list_1 = sol.create_linked_list([9,9,9,9,9,9,9])
    test_list_2 = sol.create_linked_list([9,9,9,9])
    print("Method 3 (Optimal):", sol.addTwoNumbers_optimal(test_list_1,test_list_2))


