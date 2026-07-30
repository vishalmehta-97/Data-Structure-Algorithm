class ListNode:
    def __init__(self, val=0, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

class Solution:

    def create_multilevel_linked_list(self,arrays):
        if not arrays:
            return None

        heads = []
        for arr in arrays:
            if not arr:
                heads.append(None)
                continue
            head = ListNode(arr[0])
            temp = head
            for val in arr[1:]:
                temp.child = ListNode(val)
                temp = temp.child
            heads.append(head)
        for i in range(len(heads) - 1):
            heads[i].next = heads[i + 1]
        return heads[0]
    
    ''' Brute Force '''
    def create_linked_list(self,elements):
        if not elements:
            return None
        head = ListNode(elements[0])
        current = head

        for val in elements[1:]:
            current.child = ListNode(val)
            current = current.child
        return head

    def flattenLinkedList(self,head):
        array=[]
        temp=head
        while temp:
            child_walk=temp
            while child_walk:
                array.append(child_walk.val)
                child_walk=child_walk.child
            temp=temp.next
        array.sort()

        head=self.create_linked_list(array)

    ''' Optimal Approach '''

    def mergingTwoList(self,list1,list2):
        dummy_node=ListNode(-1)
        result=dummy_node

        while list1 and list2:
            if list1.val<list2.val:
                result.child=list1
                result=list1
                list1=list1.child
            else:
                result.child=list2
                result=list2
                list2=list2.child
            result.next=None
        if list1:
            result.child=list1
        else:
            result.child=list2
        if dummy_node.child:
            dummy_node.child.next=None

        return dummy_node.child

    def flattenLinkedList_opt(self,head):
        if head==None or head.next==None:
            return head
        merge_head=self.flattenLinkedList_opt(head.next)
        return self.mergingTwoList(head,merge_head)
        
    
    def print_child_list(self,head):
        while head:
            print(head.val, end=" -> ")
            head = head.child
        print("None")

if __name__ == "__main__":
    arrays = [
        [3],
        [2, 10],
        [1, 7, 11, 12],
        [4, 9],
        [5, 6, 8]
    ]

    sol = Solution()
    head = sol.create_multilevel_linked_list(arrays)
    ans = sol.flattenLinkedList_opt(head)
    sol.print_child_list(ans)
