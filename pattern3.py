
count=7
for i in range(6):
    for k in range(count):
        print(" ",end=" ")
    for j in range(i):
        print("*",end="")
        count=count-1
    print("")    
