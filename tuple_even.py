n=(1,2,3,4,5,6,7,8,9,10)
le=len(n)
n2=[]
for i in range(le):
    if n[i]%2==0:
        n2.append(n[i])
    else:
        continue
print(tuple(n2))
