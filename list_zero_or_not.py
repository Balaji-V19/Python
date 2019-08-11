n=int(input("Enter the number"))
ls=[]
for i in range(n):
    ls.append(int(input("Enter the numbersss")))
le=len(ls)
for i in range(le-1):
    for j in range(1,le):
        if ls[i]+ls[j]==0:
            print(ls[j],ls[i])
        else:
            continue
    
