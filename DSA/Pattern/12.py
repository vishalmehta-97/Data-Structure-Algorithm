
n = 5

for i in range(1, n):
    # Left side: 1 to i
    for j in range(1, i+1):
        print(j, end="")
    
    # Middle spaces: 2*(n-i)
    for k in range(2*(n-i-1)):
        print(" ", end="")
    
    # Right side: i to 1
    for l in range(i, 0, -1):
        print(l, end="")
    
    print()

