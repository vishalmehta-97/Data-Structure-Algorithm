class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Solution:

    '''Brute Force Approach'''

    def findPairsWithGivenSum(self, head, target):
        array=[]
        t1=head
        while t1:
            t2=t1.next
            while t2 and (t1.val+t2.val<=target):
                sum=t1.val+t2.val
                if sum==target:
                    array.append([t1.val,t2.val])
                t2=t2.next
            t1=t1.head
        return array
            

    '''Better Approach'''
    def findPairsWithGivenSum_(self, head, target):
        max_limit=target-head.val
        hash={}
        array=[]
        t1=head
        while t1:
            if t1.val>max_limit:
                break
            else:
                pending_sum=target-t1.val
                if pending_sum in hash.keys():
                    arr=[hash.get(pending_sum),pending_sum]
                    array.append(arr)
                else:
                    hash[pending_sum]=t1.val
            t1=t1.next

        return array


    ''' Optimal Approach '''

    def find_tail(self,head):
        tail=head
        while tail.next:
            tail=tail.next
        return tail
    
    def findPairsWithGivenSum_(self, head, target):
        array=[]

        if head==None:
            return array
        
        l=head
        r=self.find_tail(head)

        while l.val<r.val:
        # while l != r and l.prev != r:  ## this also can be used here
            sum=l.val+r.val
            if sum>target:
                r=r.prev
            elif sum<target:
                l=l.next
            else:
                array.append([l.val,r.val])
                l=l.next
                r=r.prev
        return array

            