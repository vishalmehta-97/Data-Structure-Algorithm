def pattern22(n):

    for i in range(n):
        for j in range(n):
            if (i==0 or j==0 or i==n-1 or j==n-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

list=[z for z in range(1,10,2)]  
print(list)  
for x in list:
    pattern22(x)
