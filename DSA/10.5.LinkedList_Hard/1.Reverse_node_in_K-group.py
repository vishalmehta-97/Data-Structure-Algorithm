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

    def reverse_sll(self,head):
        t1=head
        previous=None
        while t1:
            front=t1.next
            t1.next=previous
            previous=t1
            t1=front
            head=previous

        return head

    def findKthNode(self,temp,k):
        k-=1
        while temp!=None and k>0:
            k-=1
            temp=temp.next
        return temp

    
    def reverseKGroup(self,head,k):
        temp=head
        previous=None
        while temp:
            kth_node=self.findKthNode(temp,k)
            if kth_node==None:
                if previous:
                    previous.next=temp
                break
            else:
                next_node=kth_node.next
                kth_node.next=None
                new_head=self.reverse_sll(temp)
                if temp==head:
                    head=kth_node
                else:
                    previous.next=kth_node
                previous=temp
                temp=next_node
        

        return head
    
if __name__ == "__main__":
    sol = Solution()

    test_list_1 = sol.create_linked_list([1,2])
    ele=3
    print("Ans: ", sol.reverseKGroup(test_list_1,ele))
