n=4

for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print(chr(65+k),end=" ")
    for l in range(i-1,-1,-1):
        print(chr(65+l),end=" ")
    print()