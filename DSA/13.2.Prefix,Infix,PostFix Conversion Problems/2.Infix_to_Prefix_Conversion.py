class Solution: 
    def infixToPostfix(self, s: str) -> str:
        ans=""
        stack=[]
        operators=["(",")","+","-","*","/","^"]
        mapping={
            "+":1,"-":1,
            "*":2,"/":2,
            "^":3,
            "(":0,")":0
        }
        
        for chr in s:
            if chr not in operators:
                ans+=chr     
            else:
                if chr=="(":
                    stack.append(chr)
                elif chr==")":
                    while stack[-1]!="(":
                        ans+=stack.pop()
                    stack.pop()
                else:
                    if chr=="^":
                        while stack and mapping[chr]==mapping[stack[-1]]:
                            ans+=stack.pop()
                    else:
                        while stack and mapping[chr]<mapping[stack[-1]]:
                            ans+=stack.pop()
                    stack.append(chr)
                    
        while stack:
            ans+=stack.pop()

        newans=ans[::-1]
        return newans

    def main(self,s):
        reversed_s=""
        for i in range(len(s)-1,-1,-1):
            if s[i]=="(":
                reversed_s+=")"
            elif s[i]==")":
                reversed_s+="("
            else:
                reversed_s+=s[i]

        return self.infixToPostfix(reversed_s)
        

    
ss=Solution()
# s="a+b*c"
# s="(a+b)*c"
# s="k+l-m*n/(o^p^q)*(r+s)*2"
# s="a+b*(c^d-e)^(f+g*h)-i"
# s="(a+b)*c-d+f"
s="f+d-c*(b+a)"
s="a*b+c/d"
print(ss.main(s))
