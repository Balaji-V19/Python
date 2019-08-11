n=int(input("Enter the number"))
ls=[]
for i in range(n):
    ls.append(int(input("Enter the value")))
le=len(ls)
for i in range(le):
    if i%2==0 and ls[i]%2!=0:
        print(ls[i],end="")
    elif i%2!=0 and ls[i]%2==0:
        print(ls[i],end="")
