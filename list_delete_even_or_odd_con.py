n=[12,24,35,70,88,120,155]
le=len(n)
li=[]
for i in range(le):
    if n[i]%5==0 and n[i]%7==0:
        continue
    else:
        li.append(n[i])
print(li)        
