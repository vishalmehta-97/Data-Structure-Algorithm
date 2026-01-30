def pattern22(n):

    for i in range(2*n-1):
        for j in range(2*n-1):
            top=i
            left=j
            right=(2*n-1)-1-j
            bottom=(2*n-1)-1-i

            minDist = min(top, bottom, left, right)
            print(n-minDist,end=" ")
        print()


pattern22(4)