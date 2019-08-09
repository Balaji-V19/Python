n=[12,24,35,70,88,120,155]
le=len(n)
n2=[]
for i in range(le):
    if i==0 or i==4 or i==5:
        continue
        
    else:
        n2.append(n[i])
    
        
print(n2)
