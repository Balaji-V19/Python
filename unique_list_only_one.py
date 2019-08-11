n=int(input("Enter the number"))
ls=[]
ls2=[]
ls3=[]
co=0
for i in range(n):
    ls.append(input("Enter the string"))
ls2=list(set(ls))
le=len(ls)
le2=len(ls2)
for i in range(0,le2):
    for j in range(0,le):
        if ls2[i]==ls[j]:
            co+=1
            if co>=2:
                ls3.append(ls2[i])
                co=0
                
        else:
            continue
le3=len(ls3)
for i in range(le3):
    ls2.remove(ls3[i])
print(ls2)
            
