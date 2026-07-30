class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def create_multilevel_linked_list(self,arrays):
        if not arrays:
            return None

        heads = []
        for arr in arrays:
            if not arr:
                heads.append(None)
                continue
            head = Node(arr[0])
            temp = head
            for val in arr[1:]:
                temp.Random = Node(val)
                temp = temp.Random
            heads.append(head)

        for i in range(len(heads) - 1):
            heads[i].next = heads[i + 1]
        return heads[0]
    
    ''' Brute Force Approach '''

    def copyRandomList(self,head):
        hash={}
        temp=head
        while temp:
            newNode=Node(temp.val)
            hash[temp]=newNode
            temp=temp.next

        temp=head
        while temp:
            copy_node=hash[temp]
            nextCopiedNode=hash[temp.next]
            copy_node.next=nextCopiedNode
            
            if temp.random==None:
                copy_node.random=None
            else:
                copiedRandom=hash[temp.random]
                copy_node.random=copiedRandom

            temp=temp.next

        return hash[head]

    ''' Optimal Approach '''    # (this is not running in the IDE)

    def copyRandomList_(self,head):
        temp=head
        # 1.Insert Copies in between
        while temp:
            front=temp.next
            new_node=Node(temp.val)
            new_node.next=front
            temp.next=new_node
            temp=front

        # 2.Connect Random Points
        temp=head
        while temp:
            copied_node=temp.next
            if temp.random!=None:
                copied_node.random=temp.random.next
            else:
                copied_node.random=None
            temp=temp.next.next
        # Extracting the Copied Linked List

        dummy_node=Node(-1)
        res=dummy_node
        temp=head
        while temp:
            res.next=temp.next
            res=res.next
            temp.next=temp.next.next
            temp=temp.next

        return dummy_node.next

                
    def print_Random_list(self,head):
        while head:
            print(head.val, end=" -> ")
            head = head.Random
        print("None")

if __name__ == "__main__":
    arrays =[[7,None],[13,0],[11,4],[10,2],[1,0]]

    sol = Solution()
    head = sol.create_multilevel_linked_list(arrays)
    ans = sol.copyRandomList_(head)
    sol.print_Random_list(ans)

