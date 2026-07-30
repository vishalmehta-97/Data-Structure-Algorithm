class Solution:
    ## Binary Exponentiation
    MOD = 10**9 + 7
    def myPow_(self, x: float, n: int) -> float:
        if n==0:
            return 1
        half=self.myPow_(x,n//2)
        result=(half*half)%self.MOD
        if n%2==1:
            result=(result*x)%self.MOD
        return result
    

    def countGoodNumbers(self, n: int) -> int:
        even=(n+1)//2
        odd=n//2

        return (self.myPow_(5,even)*self.myPow_(4,odd))%self.MOD
        
    
s=Solution()
n=1
n=4
n=50
# n=51
print(s.countGoodNumbers(n))