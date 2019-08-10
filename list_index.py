n=int(input("Enter the n value"))
ls=[]
co=0
for i in range(n):
    ls.append(int(input()))
le=len(ls)
for i in range(le):
    if ls[i]==i:
        print(i)
        co=1
    
if co==0:
    print(int(-1))

    
