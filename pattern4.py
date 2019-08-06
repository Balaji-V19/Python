n=7
for i in range(6):
    for j in range(n):
        print(" ",end=" ")
    for k in range(i):
        print("*",end=" ")
    n=n-1
    print(" ")
    
