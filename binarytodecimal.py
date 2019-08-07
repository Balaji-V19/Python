bn=list(input("enter the list").split(","))
le=len(bn)
dec=[]
for i in range(le):
    dec.append(int(bn[i],2))
for i in range(le):
    if dec[i]%5==0:
        print(bn[i])

    
