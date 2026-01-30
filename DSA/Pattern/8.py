n = 5
for i in range(n, 0, -1):
    for s in range(n - i):
        print(" ", end="")
    for j in range(2*i - 1):
        print("*", end="")
    print()
