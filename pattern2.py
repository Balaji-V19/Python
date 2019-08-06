spc=-1
for i in range(6,0,-1):
    spc+=2
    for k in range(spc):
        print(" ",end="")
    for j in range(i):
        print("*",end=" ")
    print()
      
