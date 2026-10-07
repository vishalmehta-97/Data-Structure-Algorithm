from typing import List

''' Optimal Approach'''
         
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for i in range(len(asteroids)):
            if asteroids[i]>0:
                stack.append(asteroids[i])
            else:
                while stack and stack[-1]>0 and stack[-1]<abs(asteroids[i]):
                    stack.pop()

                if stack and stack[-1]==abs(asteroids[i]):
                    stack.pop()
                elif not stack or stack[-1]<0:
                    stack.append(asteroids[i])

        return stack


s=Solution()
asteroids=[4,7,1,1,2,-3,-7,17,15,-16]
# asteroids=[5,10,-5]
# asteroids=[-2,2,1,-2]
print(s.asteroidCollision(asteroids))
         