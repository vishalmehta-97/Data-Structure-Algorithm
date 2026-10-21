class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum>num*9:
            return ""
        ans=""
        total_nines=sum//9
        remaining_sum=sum%9

        while total_nines!=0:
            ans+=str(9)
            total_nines-=1

        if remaining_sum>0:
            ans+=str(remaining_sum)

        if len(ans)<num:
            while len(ans)!=num:
                ans+=str(0)
        return ans

s=Solution()
num=2
sum=18
print(s.maxSumOfSquares(num,sum))