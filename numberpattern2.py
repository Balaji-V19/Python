n=1
temp=0
su=0
for i in range(6):
    if su > 0:
        n=su
    for j in range(0,i):
        n=n+1
    su=n
    temp=su
    for k in range(0,i):
        su=su-1
        print(su,end="  ")
        su=su+2
    su=temp-1
    #print(su)
    print()
        
        
