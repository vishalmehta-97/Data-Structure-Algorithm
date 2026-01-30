n=5

for i in range(1,n+1):
    for j in range(i):
        print("*", end=" ")
    for k in range(2*(n-i)):
        print(" ",end=" ")
    for l in range(i):
        print("*",end=" ")
    print()
for a in range(1,n):
    for b in range(n-a):
        print("*",end=" ")
    for c in range(2*a):
        print(" ",end=" ")
    for d in range(n-a):
        print("*",end=" ")
    print()



