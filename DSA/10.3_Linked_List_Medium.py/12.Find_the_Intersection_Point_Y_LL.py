class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
    '''Brute Force Approach'''

    def getIntersectionNode(self,headA,headB): 
        hash={}

        t1=headA
        t2=headB

        while t1:
            hash[t1]=1
            t1=t1.head

        while t2:
            if t2 in hash.keys():
                return t2
            t2=t2.next

        return
    
    ''' Better Approach '''

    def getIntersectionNode_(self,headA,headB): 
        t1=headA
        t2=headB
        countA=0
        while t1:
            countA+=1
            t1=t1.next

        countB=0
        while t2:
            countB+=1
            t2=t2.next

        if countA>countB:
            d=countA-countB
            
        else:
            d=-(countB-countA)
        
        t1=headA
        t2=headB
        if d>0:   ## We can also make a different function here named like Collesion Point
            while d!=0:
                d-=1
                t1=t1.next

        else:
            d=-d
            while d!=0:
                d-=1
                t2=t2.next

        while t1:
            if t1==t2:
                return t1
            t1=t1.next 
            t2=t2.next 
    
        return


    '''Brute Force Approach'''

    def getIntersectionNode(self,headA,headB): 
        hash={}

        t1=headA
        t2=headB

        while t1:
            hash[t1]=1
            t1=t1.head

        while t2:
            if t2 in hash.keys():
                return t2
            t2=t2.next

        return
    
    ''' Optimal Approach '''

    def getIntersectionNode_(self,headA,headB): 
        if headA==None and headB==None:
            return

        t1=headA
        t2=headB

        while t1!=t2:
            t1=t1.next
            t2=t2.next

            if t1==t2:
                return t1
            
            if t1==None:
                t1=headB
            if t2==None:
                t2=headA
                
        return t1
        
        
        
        




    


        