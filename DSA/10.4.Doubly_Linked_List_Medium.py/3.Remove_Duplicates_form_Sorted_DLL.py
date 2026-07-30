class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class Solution:
    def create_dll(self, arr):
        if not arr:
            return None

        head = ListNode(arr[0])
        t1 = head

        for i in range(1, len(arr)):
            new_node = ListNode(arr[i])
            t1.next = new_node
            new_node.prev = t1
            t1 = new_node

        return head


    def print_dll(self, head):
        t1 = head

        while t1:
            print(t1.val, end=" <-> ")
            t1 = t1.next

        print("None")

    '''Brite Force Approach '''
    # def removeDuplicates(self, head):
    #     if head==None or head.next==None:
    #         return head
        
    #     hash={}
    #     t1=head
    #     while t1:
    #         hash[t1.val]=hash.get(t1.val,0) + 1
    #         t1=t1.next
    #     t1=head
    #     previous=None
    #     for ele in hash:
    #         t1.val=ele
    #         previous=t1
    #         t1=t1.next
    #     if previous:
    #         previous.next=None
    #     return head

    ''' Optimal Approach '''
    def removeDuplicates(self, head):
        if head==None or head.next==None:
                return head

        previous=None
        t1=head

        while t1:
            if t1.next==None:
                previous.next=t1
                t1.prev=previous
                break

            if t1.next.val==t1.val:
                t1=t1.next
            elif t1.next.val!=t1.val:
                if previous:
                    previous.next=t1
                else:
                    head=t1
                t1.prev=previous
                previous=t1
                t1=t1.next

        return head

    ''' Optimal Approach '''

    def removeDuplicates(self, head):
        temp=head

        while temp and temp.next:
            next_node=temp.next

            while next_node!=None and next_node.val==temp.val:
                next_node=next_node.next

            temp.next=next_node
            if next_node:
                next_node.prev=temp
            temp=temp.next

        return head



if __name__ == "__main__":

    sol=Solution()

    arr = [1,1]
    head = sol.create_dll(arr)

    print("Original DLL:")
    sol.print_dll(head)
    head = sol.removeDuplicates(head)

    print("After Removing Duplicates:")
    sol.print_dll(head)
            