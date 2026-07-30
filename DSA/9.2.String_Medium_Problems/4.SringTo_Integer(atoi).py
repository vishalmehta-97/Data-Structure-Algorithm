
def myAtoi(s):
    s= s.strip()
    sign=1
    ans=0
    if len(s)==0:
        return 0
    if s[0]=='-' or s[0]=='+':
        if s[0]=='-':
            sign=-1
        s=s[1:]

    for char in s:
        if not char.isdigit():
            break
        ans=ans*10+int(char)

    ans=ans*sign

    if ans<-2**31:
        return -2**31
    elif ans>2**31-1:
        return 2**31-1
    else:
        return ans



s="42"
s="1337c0d3"
s="0-1"
s="words and 987"
s=" -042"
print(myAtoi(s))
    