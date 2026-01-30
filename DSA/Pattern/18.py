n=5

for i in range(1,n+1):
    for j in range(i-1,-1,-1):
        print(chr(69-j), end=" ")
    print()
