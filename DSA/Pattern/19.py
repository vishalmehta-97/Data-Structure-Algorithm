n=5

for i in range(n):
    for j in range(n-i,0,-1):
        print("*", end=" ")
    for k in range(2*i):
        print(" ",end=" ")
    for l in range(n-i):
        print("*",end=" ")
    print()
for a in range(1,n+1):
    for b in range(a):
        print("*",end=" ")
    for c in range(2*(n-a)):
        print(" ",end=" ")
    for d in range(a):
        print("*",end=" ")
    print()
    