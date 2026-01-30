n=5

for i in range(1,n+1):
    for j in range(i):
        if (i + j) % 2 == 0:
            print("0",end=" ")
        else:
            print("1",end=" ")
            # i=i-1
    print()
  