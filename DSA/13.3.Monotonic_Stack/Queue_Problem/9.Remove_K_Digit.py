class Solution:
    def helper(self,num,k,ans,index,mini):
        if len(ans)==len(num)-k:
            mini=min(mini,int(ans))

            if index>=len(num):
                return mini

        for i in range(len(num)):
            if not ans and num[i]==0:
                continue
            else:
                self.helper(num,k,ans+num[i],index+1,mini)
                self.helper(num,k,ans,index+1,mini)
            return
    def removeKdigits(self, num: str, k: int) -> str:
        ans=""
        return self.helper(num,k,ans,index=0,mini=float("inf"))

s=Solution()
num="1432219"
k=3
# print(s.removeKdigits(num,k))


# class Solution:

#   def removeKdigits(self, num: str, k: int) -> str:
#     target_len = len(num) - k
#     if target_len == 0:
#       return "0"

#     min_val = [float("inf")]

#     def backtrack(index: int, current: str):
#       # If we built a number of the required length
#       if len(current) == target_len:
#         min_val[0] = min(min_val[0], int(current))
#         return

#       # Prune branches if there aren't enough digits left to reach target_len
#       digits_left = len(num) - index
#       if len(current) + digits_left < target_len:
#         return

#       # Choice 1: Take num[index]
#       backtrack(index + 1, current + num[index])

#       # Choice 2: Skip num[index]
#       backtrack(index + 1, current)

#     backtrack(0, "")
#     return str(min_val[0])


''' Optimal Approach '''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k==len(num):
            return "0"
        stack=[]
        for i in range(len(num)):
            if k>0:
                while stack and k>0 and int(stack[-1])>int(num[i]):
                    stack.pop()
                    k-=1
                stack.append(num[i])
                index=i

        for i in range(index+1,len(num)):
            stack.append(num[i])

        while k>0:
            stack.pop()
            k-=1

        if not stack: 
            return "0"
        
        ans=""
        for i in range(len(stack)-1,-1,-1):
            ans+=stack[i]
        n=len(ans)
        while n!=0 and ans[-1]=="0":
            n=n-1
            ans=ans[:n+1]

        return ans[::-1]
s=Solution()
num="1432219"
num="10200"
# num="100"
k=1
# k=1
print(s.removeKdigits(num,k))