'''
Infix: We use infix heavily , Most of the programming languages 
       like C,C++,Java Understand Infix.

PostFix: These are used in Stackbased Calculators.

PreFix: This is used extensively which is known as List . 
        It is also used in Tree Data Structures.
'''
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
                elif chr=="+" or chr =="-":
                    if not stack:
                        stack.append(chr)
                    else:
                        if mapping[stack[-1]]<mapping[chr]:
                            stack.append(chr)
                        else:
                            while stack and (mapping[stack[-1]]>=mapping[chr]):
                                ans+=stack.pop()
                            stack.append(chr)
                elif chr=="*" or chr=="/":
                    if not stack:
                        stack.append(chr)
                    else:
                        if mapping[stack[-1]]<mapping[chr]:
                            stack.append(chr)
                        else:
                            while stack and (mapping[stack[-1]]>=mapping[chr]):
                                ans+=stack.pop()
                            stack.append(chr)

                elif chr=="^":
                    if not stack:
                        stack.append(chr)
                    else:
                        stack.append(chr)

        while stack:
            ans+=stack.pop()

        return ans
    
ss=Solution()
s="a+b*c"
s="(a+b)*c"
s="k+l-m*n/(o^p^q)*(r+s)*2"
s="a+b*(c^d-e)^(f+g*h)-i"
# print(ss.infixToPostfix(s))


''' More Optimal In Code Structure '''

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
                else:      # ALL OPERATORS CODE WAS REDUNDENT ON THE PREVIOUS CODE
                    if not stack:
                        stack.append(chr)
                    else:
                        if mapping[stack[-1]]<mapping[chr]:
                            stack.append(chr)
                        else:
                            while stack and (mapping[stack[-1]]>=mapping[chr]):
                                ans+=stack.pop()
                            stack.append(chr)
                

        while stack:
            ans+=stack.pop()

        return ans
    
ss=Solution()
s="a+b*c"
s="(a+b)*c"
s="k+l-m*n/(o^p^q)*(r+s)*2"
s="a+b*(c^d-e)^(f+g*h)-i"
print(ss.infixToPostfix(s))