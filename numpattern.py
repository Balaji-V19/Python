n=0
dec=18
for i in range(6):
    for sp in range(0,dec):
        print(" ",end="")
    for j in range(0,i):
        n=n+1
    su=n
    temp=su
    for k in range(0,i):
        print(su,end="  ")
        su=su-1
    su=temp
    dec=dec-2
    print()    
