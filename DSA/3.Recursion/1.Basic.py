''' When a function calls itself Until a Specified conditoin met '''

def counting(c):
    if c>100:
        return
    
    print(c,end=" ")
    counting(c+1)

counting(1)

print()

def ginti(n):
    if n<=0:
        return
    ginti(n-1)
    print(n,end=" ")

ginti(100)

print()
print()

def evenOnly(n):
    if n<=0:
        return
    
    evenOnly(n-1)
    
    if n%2==0:
        print(n,end=" ")


evenOnly(10)
