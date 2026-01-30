n=5

# for i in range(n):
#     for j in range(n,i,-1):
#         print(chr(70-j),end=" ")
#     print()

# this was also good but if the n's value changes it will not work


for i in range(n):           
    for j in range(n-i):
        print(chr(65 + j), end="")
    print()