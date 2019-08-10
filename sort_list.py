n=int(input("Enter the number"))
ls=[]
ls1=[]
co=0
for i in range(n):
    ls.append(input())

if len(ls) == len(set(ls)):
    print("No Repeated Values here")
else:
    le=len(ls)
    for i in range(le-1):
        for j in range(i+1,le):
            if ls[i]==ls[j]:
                ls1.append(ls[j])
            else:
                continue
ls1.sort()
print(ls1)
                
