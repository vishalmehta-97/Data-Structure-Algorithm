n=5

for i in range(n+1):
    print(i*"*")
    

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()    
