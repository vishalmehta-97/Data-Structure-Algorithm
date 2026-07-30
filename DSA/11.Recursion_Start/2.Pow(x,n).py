class Solution:
    ''' Brute Force Approach '''

    def myPow(self, x: float, n: int) -> float:
        ans=1.0
        nn=n
        if nn<0:
            nn=-nn
        for i in range(n):
            ans=ans*x

        if n<0:
            return 1.0/ans
        else:
            return ans
        
    '''Better Approach'''

    def myPow_(self, x: float, n: int) -> float:
        if n<0:
            nn=n
            nn=-nn
        ans = 1
        while nn > 0:
            if nn % 2 == 1:
                ans *= x
            x *= x
            nn = nn // 2
        # while nn>0:
        #     if nn%2==0:
        #         x*=x
        #         nn=nn//2   ## nn has to be remain int not double
        #     else:
        #         ans*=x
        #         nn-=1

        if n<0:
            return 1.0/ans
        return ans




s=Solution()
print(s.myPow_(x=2.0000,n=-2))