n=str(input("Enter the string"))
le=len(n)
for i in range(le):
    if i%2==0:
        print(n[i],end="")
    else:
        continue
