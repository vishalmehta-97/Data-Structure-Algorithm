n=5
alpha=["A"]

for i in range(n):
    for j in range(i+1):
        print(chr(65+j),end=" ")
    print()