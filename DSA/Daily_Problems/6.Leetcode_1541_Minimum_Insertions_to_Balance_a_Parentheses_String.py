class Solution:
    def minInsertions(self, s: str) -> int:
        count=0
        result=0 # Insertions
        i=0

        while i<len(s):
            if s[i]=="(":
                count+=1
                i+=1
            else:
                if count>0:
                    count-=1  
                else:
                    result+=1
                
                if i+1<len(s) and s[i+1]==")":
                    i+=2
                else:
                    result+=1
                    i+=1

        return result+(count*2)


s=Solution()
ss="(()))"
ss="))())("
print(s.minInsertions(ss))