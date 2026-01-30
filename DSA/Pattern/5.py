n=5

# for i in range(5,0,-1):
#     print(i*"*")

for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()